import sys
import click
from cffconvert.citation import Citation
from cffconvert.bibtex import BibtexObject
from cffconvert.codemeta import CodemetaObject
from cffconvert.endnote import EndnoteObject
from cffconvert.ris import RisObject
from cffconvert.schemaorg import SchemaorgObject
from cffconvert.zenodo import ZenodoObject
from cffconvert.apalike import ApalikeObject
from cffconvert.version import __version__ as cffconvert_version


format_choices = ["bibtex", "cff", "codemeta", "endnote", "ris", "schema.org", "zenodo", "apalike"]


@click.command(context_settings=dict(max_content_width=120))
@click.option("-i", "infile", type=str, default=None, help="Path to the CITATION.cff input file. Use '-i -' to read from STDIN.")
@click.option("-o", "outfile", type=str, default=None,help="Path to the output file.")
@click.option("-f", "outputformat", type=click.Choice(format_choices), default=None, help="Output format.")
@click.option("-u", "--url", type=str, default=None, help="URL of the repo containing the CITATION.cff (currently only github.com is supported; may " +
              "include branch name, commit sha, tag name). For example: 'https://github.com/citation-file-format/cff-converter-python' or 'https://g" +
              "ithub.com/citation-file-format/cff-converter-python/tree/main'")
@click.option("-h", "--help", "show_help", is_flag=True, flag_value=True, default=False, help="Show help and exit.")
@click.option("--show-trace", "show_trace", is_flag=True, flag_value=True, default=False, help="Show error trace.")
@click.option("--validate", is_flag=True, default=False, help="Validate the CITATION.cff found at the URL or supplied through '-i'.")
@click.option("--ignore-suspect-keys", "ignore_suspect_keys", is_flag=True, default=False, help="Ignore any keys from CITATION.cff that are l" +
              "ikely out of date, such as 'commit', 'date-released', 'doi', and 'version'.")
@click.option("--verbose", is_flag=True, default=False, help="Provide feedback on what was entered.")
@click.option("--version", is_flag=True, default=False, help="Print version and exit.")
def cli(infile, outfile, outputformat, url, show_help, show_trace, validate, ignore_suspect_keys, verbose, version):

    def print_help():
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

    no_user_input = len(sys.argv) == 1
    if show_help or no_user_input:
        print_help()

    if show_trace is False:
        sys.tracebacklimit = 0

    if version is True:
        print("{0}".format(cffconvert_version))
        return

    if verbose is True:
        click.echo("{0} = {1}".format("infile", infile))
        click.echo("{0} = {1}".format("outfile", outfile))
        click.echo("{0} = {1}".format("outputformat", outputformat))
        click.echo("{0} = {1}".format("url", url))
        click.echo("{0} = {1}".format("show_trace", show_trace))
        click.echo("{0} = {1}".format("validate", validate))
        click.echo("{0} = {1}".format("ignore_suspect_keys", ignore_suspect_keys))
        click.echo("{0} = {1}".format("verbose", verbose))
        click.echo("{0} = {1}".format("version", version))

    if infile is None and url is None:
        infile = "CITATION.cff"
    elif infile is not None and url is not None:
        raise ValueError("You need to specify either an input file or a URL, but not both.")

    if infile is None:
        cffstr = None
    elif infile == '-':
        cffstr = sys.stdin.read()
    else:
        with open(infile, "r", encoding="utf8") as f:
            cffstr = f.read()

    # TODO currently there is no way to provide values for these 3 arguments from the command line
    remove = None
    override = None
    suspect_keys = None

    # url, ignore_suspect_keys=ignore_suspect_keys, override=override, remove=remove,
    # suspect_keys=suspect_keys, validate=validate

    citation = Citation(cffstr)

    if validate is True:
        citation.validate()

    if outputformat is None:
        return
    elif outputformat == "bibtex":
        outstr = BibtexObject(citation.cffobj).print()
    elif outputformat == "cff":
        outstr = citation.cffstr
    elif outputformat == "codemeta":
        outstr = CodemetaObject(citation.cffobj).print()
    elif outputformat == "endnote":
        outstr = EndnoteObject(citation.cffobj).print()
    elif outputformat == "ris":
        outstr = RisObject(citation.cffobj).print()
    elif outputformat == "schema.org":
        outstr = SchemaorgObject(citation.cffobj).print()
    elif outputformat == "zenodo":
        outstr = ZenodoObject(citation.cffobj).print()
    elif outputformat == "apalike":
        outstr = ApalikeObject(citation.cffobj).print()

    if outfile is None:
        print(outstr, end='')
    else:
        with open(outfile, "w", encoding="utf8") as f:
            f.write(outstr)


if __name__ == "__main__":
    cli()
