import os
import sys
import click
from cffconvert.cli.check_early_exits import check_early_exits
from cffconvert.cli.create_citation import create_citation
from cffconvert.cli.validate_or_write_output import validate_or_write_output


options = {
    "infile": {
        "type": click.Path(),
        "default": None,
        "help": "Path to the CITATION.cff input file. If this option is omitted" +
                f", '.{os.sep}CITATION.cff' is used."
    },
    "outfile": {
        "type": click.Path(),
        "default": None,
        "help": "Path to the output file."
    },
    "outputformat": {
        "type": click.Choice([
            "apalike",
            "bibtex",
            "cff",
            "codemeta",
            "endnote",
            "ris",
            "schema.org",
            "zenodo"
        ]),
        "default": None,
        "help": "Output format."
    },
    "url": {
        "type": str,
        "default": None,
        "help": "URL to the CITATION.cff input file."
    },
    "show_help": {
        "is_flag": True,
        "flag_value": True,
        "default": False,
        "help": "Show help and exit."
    },
    "show_trace": {
        "is_flag": True,
        "flag_value": True,
        "default": False,
        "help": "Show error trace."
    },
    "validate_only": {
        "is_flag": True,
        "default": False,
        "help": "Validate the CITATION.cff file and exit."
    },
    "version": {
        "is_flag": True,
        "default": False,
        "help": "Print version and exit."
    },
    "verbose": {
        "is_flag": True,
        "default": False,
        "help": "Control output verbosity."
    }
}
epilog = """If this program is useful to you, consider giving it a star on GitHub:
https://github.com/citation-file-format/cffconvert"""


@click.command(epilog=epilog)
@click.option("-i", "--infile", "infile", **options["infile"])
@click.option("-o", "--outfile", "outfile", **options["outfile"])
@click.option("-f", "--format", "outputformat", **options["outputformat"])
@click.option("-u", "--url", "url", **options["url"])
@click.option("-h", "--help", "show_help", **options["show_help"])
@click.option("--show-trace", "show_trace", **options["show_trace"])
@click.option("--validate", "validate_only", **options["validate_only"])
@click.option("--version", "version", **options["version"])
@click.option("--verbose", "verbose", **options["verbose"])
# pylint: disable=too-many-arguments
def cli(infile, outfile, outputformat, url, show_help, show_trace, validate_only, version, verbose):
    """Command line program to validate and convert CITATION.cff files."""

    check_early_exits(show_help, version)

    if show_trace is False:
        # show elaborate error details if something goes wrong
        sys.tracebacklimit = 0

    # if user didn't specify a filename or a url, apply default filename
    if infile is None and url is None:
        infile = "CITATION.cff"

    # load the citation metadata from the specified source and create a Python object representation of it
    citation = create_citation(infile, url)

    # either validate and exit, or convert to the selected output format
    validate_or_write_output(outfile, outputformat, validate_only, citation, verbose)
