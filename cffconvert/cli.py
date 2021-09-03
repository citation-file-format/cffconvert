import os
import sys
import click
import pykwalify
import jsonschema
from cffconvert.citation import Citation
from cffconvert.version import __version__ as cffconvert_version


options = {
    "infile": dict(
        type=click.Path(),
        default=".{0}CITATION.cff".format(os.sep),
        help="Path to the CITATION.cff input file. Default value is '.{0}CITATION.cff'.".format(os.sep)
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
    "validate": dict(
        is_flag=True,
        default=False,
        help="Validate the CITATION.cff and exit."
    ),
    "ignore_suspect_keys": dict(
        is_flag=True,
        default=False,
        help="Ignore any keys from CITATION.cff that are likely out of date, such as 'commit', 'date-released', 'doi', and 'version'."
    ),
    "verbose": dict(
        is_flag=True,
        default=False,
        help="Provide feedback on what was entered."
    ),
    "version": dict(
        is_flag=True,
        default=False,
        help="Print version and exit."
    )
}


@click.command(context_settings=dict(max_content_width=120))
@click.option("-i", "infile", **options["infile"])
@click.option("-o", "outfile", **options["outfile"])
@click.option("-f", "outputformat", **options["outputformat"])
@click.option("-h", "--help", "show_help", **options["show_help"])
@click.option("--show-trace", "show_trace", **options["show_trace"])
@click.option("--validate", "validate", **options["validate"])
@click.option("--ignore-suspect-keys", "ignore_suspect_keys", **options["ignore_suspect_keys"])
@click.option("--verbose", "verbose", **options["verbose"])
@click.option("--version", "version", **options["version"])
def cli(infile, outfile, outputformat, show_help, show_trace, validate, ignore_suspect_keys, verbose, version):

    def print_help():
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    if verbose is True:
        click.echo("{0} = {1}".format("infile", infile))
        click.echo("{0} = {1}".format("outfile", outfile))
        click.echo("{0} = {1}".format("outputformat", outputformat))
        click.echo("{0} = {1}".format("show_help", show_help))
        click.echo("{0} = {1}".format("show_trace", show_trace))
        click.echo("{0} = {1}".format("validate", validate))
        click.echo("{0} = {1}".format("ignore_suspect_keys", ignore_suspect_keys))
        click.echo("{0} = {1}".format("verbose", verbose))
        click.echo("{0} = {1}".format("version", version))

    no_user_input = len(sys.argv) == 1
    if show_help or no_user_input:
        print_help()
        return

    if show_trace is False:
        sys.tracebacklimit = 0

    if version is True:
        print("{0}".format(cffconvert_version))
        return

    with open(infile, "r", encoding="utf8") as f:
        cffstr = f.read()

    # url, ignore_suspect_keys=ignore_suspect_keys
    # validate=validate

    citation = Citation(cffstr)

    if validate is True:
        citation.validate()
        print("'{0}' is valid.".format(infile))
        return

    if outputformat is None:
        return

    try:
        citation.validate()
    except (pykwalify.errors.SchemaError, jsonschema.exceptions.ValidationError) as e:
        print("'{0}' does not pass validation. Conversion aborted.".format(infile))
        return
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


if __name__ == "__main__":
    cli()
