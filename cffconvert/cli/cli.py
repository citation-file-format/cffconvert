import os
import sys
import click
from cffconvert.cli.check_early_exits import check_early_exits
from cffconvert.cli.create_citation import create_citation
from cffconvert.cli.validate_or_write_output import validate_or_write_output


options = {
    "infile": dict(
        type=click.Path(),
        default=None,
        help="Path to the CITATION.cff input file. If this option is omitted" +
             f", '.{os.sep}CITATION.cff' is used."
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
        help="Validate the CITATION.cff file and exit."
    ),
    "version": dict(
        is_flag=True,
        default=False,
        help="Print version and exit."
    )
}


@click.command()
@click.option("-i", "--infile", "infile", **options["infile"])
@click.option("-o", "--outfile", "outfile", **options["outfile"])
@click.option("-f", "--format", "outputformat", **options["outputformat"])
@click.option("-u", "--url", "url", **options["url"])
@click.option("-h", "--help", "show_help", **options["show_help"])
@click.option("--show-trace", "show_trace", **options["show_trace"])
@click.option("--validate", "validate_only", **options["validate_only"])
@click.option("--version", "version", **options["version"])
# pylint: disable=too-many-arguments
def cli(infile, outfile, outputformat, url, show_help, show_trace, validate_only, version):

    check_early_exits(show_help, version)

    if show_trace is False:
        # show elaborate error details if something goes wrong
        sys.tracebacklimit = 0

    # if user didn't specify a filename or a url, apply default filename
    if infile is None and url is None:
        infile = 'CITATION.cff'

    # load the citation metadata from the specified source and create a Python object representation of it
    citation = create_citation(infile, url)

    # either validate and exit, or convert to the selected output format
    validate_or_write_output(outfile, outputformat, validate_only, citation)
