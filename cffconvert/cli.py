import os
import sys
import click
from jsonschema.exceptions import ValidationError as JsonschemaSchemaError
from pykwalify.errors import SchemaError as PykwalifySchemaError
from cffconvert.citation import Citation
from cffconvert.fetching import read_from_url
from cffconvert.version import __version__ as cffconvert_version


def _check_early_exits(show_help, version):
    ctx = click.get_current_context()
    if show_help or len(sys.argv) == 1:
        click.echo(ctx.get_help())
        ctx.exit()
    if version is True:
        print("{0}".format(cffconvert_version))
        ctx.exit()


def _create_citation(infile, url):
    condition = (infile is None, url is None)
    if condition == (True, True):
        # neither has been defined, raise
        raise ValueError("Define either a URL or a local file as the input.")

    if condition == (False, False):
        # both have been defined, raise
        raise ValueError("Define either a URL or a local file as the input, not both.")

    if condition == (True, False):
        cffstr = read_from_url(url)
        return Citation(cffstr, src=url)

    if condition == (False, True):
        cffstr = _read_from_file(infile)
        return Citation(cffstr, src=infile)

    raise ValueError("Something went wrong creating the citation object.")


def _read_from_file(infile):
    with open(infile, "r", encoding="utf8") as f:
        return f.read()


def _validate_or_write_output(outfile, outputformat, validate_only, citation):
    condition = (validate_only, outputformat is not None)
    if condition == (True, False):
        # just validate, there is no target outputformat
        citation.validate()
        print("Citation metadata are valid according to schema version {0}.".format(citation.cffversion))
    elif condition == (True, True):
        # just validate, ignore the target outputformat
        citation.validate()
        print("Ignoring output format. Citation metadata are valid according to " +
              "schema version {0}.".format(citation.cffversion))
    elif condition == (False, False):
        # user hasn't indicated what they want
        print('Indicate whether you want to validate or convert the citation metadata.')
    elif condition == (False, True):
        # validate the input, then write to target outputformat
        try:
            citation.validate()
        except (PykwalifySchemaError, JsonschemaSchemaError):
            print("'{0}' does not pass validation. Conversion aborted.".format(citation.src))
            ctx = click.get_current_context()
            ctx.exit()
        outstr = {
            "apalike": citation.as_apalike,
            "bibtex": citation.as_bibtex,
            "cff": citation.as_cff,
            "codemeta": citation.as_codemeta,
            "endnote": citation.as_endnote,
            "ris": citation.as_ris,
            "schema.org": citation.as_schemaorg,
            "zenodo": citation.as_zenodo
        }[outputformat]()
        if outfile is None:
            print(outstr, end='')
        else:
            with open(outfile, "w", encoding="utf8") as f:
                f.write(outstr)
    else:
        # shouldn't happen
        raise ValueError('Something went wrong validating or writing the output')


options = {
    "infile": dict(
        type=click.Path(),
        default=None,
        help="Path to the CITATION.cff input file. If option is omitted, .{0}CITATION.cff is used.".format(os.sep)
    ),
    "outfile": dict(
        type=click.Path(),
        default=None,
        help="Path to the output file."
    ),
    "outputformat": dict(
        type=click.Choice([
            "apalike",
            "bibtex",
            "cff",
            "codemeta",
            "endnote",
            "ris",
            "schema.org",
            "zenodo"
        ]),
        default=None,
        help="Output format."
    ),
    "url": dict(
        type=str,
        default=None,
        help="URL to the CITATION.cff input file."
    ),
    "show_help": dict(
        is_flag=True,
        flag_value=True,
        default=False,
        help="Show help and exit."
    ),
    "show_trace": dict(
        is_flag=True,
        flag_value=True,
        default=False,
        help="Show error trace."
    ),
    "validate_only": dict(
        is_flag=True,
        default=False,
        help="Validate the CITATION.cff and exit."
    ),
    "version": dict(
        is_flag=True,
        default=False,
        help="Print version and exit."
    )
}


@click.command()
@click.option("-i", "infile", **options["infile"])
@click.option("-o", "outfile", **options["outfile"])
@click.option("-f", "outputformat", **options["outputformat"])
@click.option("-u", "--url", "url", **options["url"])
@click.option("-h", "--help", "show_help", **options["show_help"])
@click.option("--show-trace", "show_trace", **options["show_trace"])
@click.option("--validate", "validate_only", **options["validate_only"])
@click.option("--version", "version", **options["version"])
# pylint: disable=too-many-arguments
def cli(infile, outfile, outputformat, url, show_help, show_trace, validate_only, version):

    _check_early_exits(show_help, version)

    if show_trace is False:
        # show elaborate error details if something goes wrong
        sys.tracebacklimit = 0

    # if user didn't specify a filename or a url, apply default filename
    if infile is None and url is None:
        infile = 'CITATION.cff'

    # load the citation metadata from the specified source and create a Python object representation of it
    citation = _create_citation(infile, url)

    # either validate and exit, or convert to the selected output format
    _validate_or_write_output(outfile, outputformat, validate_only, citation)
