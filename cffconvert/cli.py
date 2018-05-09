import click
from cffconvert import Citation
from cffconvert import version as cffconvert_version


@click.command(context_settings=dict(max_content_width=120))
@click.option("--infile", "-if", type=str, default=None,
              help="Path to the CITATION.cff input file.")
@click.option("--outfile", "-of", type=str, default=None,
              help="Path to the output file.")
@click.option("--outputformat", "-f", type=str, default=None,
              help="Output format: bibtex|cff|codemeta|endnote|ris|zenodo")
@click.option("--url", "-u", type=str, default=None,
              help="URL of the repo containing the CITATION.cff (currently only github.com is supported; may " +
                   "include branch name, commit sha, tag name). For example: \'https://github.com/citation-fi" +
                   "le-format/cff-converter-python\' or \'https://github.com/citation-file-format/cff-convert" +
                   "er-python/tree/master\'")
@click.option("--validate", is_flag=True, default=False,
              help="Validate the CITATION.cff found at the URL or supplied through '--infile'")
@click.option("--ignore-suspect-keys", "-ig", is_flag=True, default=False,
              help="If True, ignore any keys from CITATION.cff that are likely out of date, such as \'commit\', " +
                   "\'date-released\', \'doi\', and \'version\'.")
@click.option("--verbose", is_flag=True, default=False,
              help="Provide feedback on what was entered.")
@click.option("--version", is_flag=True, default=False,
              help="Print version and exit.")
def cli(infile, outfile, outputformat, url, validate, ignore_suspect_keys, verbose, version):

    if version is True:
        print("{0}".format(cffconvert_version.__version__))
        return

    if verbose is True:
        click.echo("{0} = {1}".format("infile", infile))
        click.echo("{0} = {1}".format("outfile", outfile))
        click.echo("{0} = {1}".format("outputformat", outputformat))
        click.echo("{0} = {1}".format("url", url))
        click.echo("{0} = {1}".format("validate", validate))
        click.echo("{0} = {1}".format("ignore_suspect_keys", ignore_suspect_keys))
        click.echo("{0} = {1}".format("verbose", verbose))
        click.echo("{0} = {1}".format("version", version))

    if infile is None and url is None:
        infile = "CITATION.cff"
    elif infile is not None and url is not None:
        raise ValueError("You need to specify either \'--infile\' or \'url\' but not both.")

    if infile is None:
        cffstr = None
    else:
        with open(infile, "r") as f:
            cffstr = f.read()

    # TODO currently there is no way to provide values for these 3 arguments from the command line
    remove = None
    override = None
    suspect_keys = None

    citation = Citation(url=url, cffstr=cffstr, ignore_suspect_keys=ignore_suspect_keys, override=override,
                        remove=remove, suspect_keys=suspect_keys, validate=validate)

    acceptable_output_formats = ["bibtex", "cff", "codemeta", "endnote", "ris", "zenodo"]
    if validate:
        pass
    elif outputformat not in acceptable_output_formats:
        raise ValueError("'--outputformat' should be one of [{0}]".format(", ".join(acceptable_output_formats)))

    if outputformat is None:
        return
    elif outputformat == "bibtex":
        outstr = citation.as_bibtex()
    elif outputformat == "codemeta":
        outstr = citation.as_codemeta()
    elif outputformat == "endnote":
        outstr = citation.as_enw()
    elif outputformat == "ris":
        outstr = citation.as_ris()
    elif outputformat == "zenodo":
        outstr = citation.as_zenodojson()
    elif outputformat == "cff":
        outstr = citation.cffstr

    if outfile is None:
        print(outstr)
    else:
        with open(outfile, "w") as f:
            f.write(outstr + "\n")
