import click
import os
from cffconvert import Citation


@click.command(context_settings=dict(max_content_width=120))
@click.option("--infile", "-if", type=str, default=None, help="Path to the CITATION.cff input file.")
@click.option("--outfile", "-of", type=str, default=None, help="Path to the output file.")
@click.option("--outputformat", "-f", type=str, default=None, help="Output format: bibtex|codemeta|endnote|ris|zenodo",
              required=True)
@click.option("--url", "-u", type=str, default=None, help="URL of the repo containing the CITATION.cff (currently only "
                                                          "github.com is supported; may include branch name, commit " +
                                                          "sha, tag name). For example: \'https://github.com/" +
                                                          "citation-file-format/cff-converter-python\' or \'https" +
                                                          "://github.com/citation-file-format/cff-converter-python/" +
                                                          "tree/master\'")
@click.option("--validate", "-v", is_flag=True, default=False, help="Validate the CITATION.cff found at the URL or " +
                                                                    "supplied through '--infile'")
@click.option("--ignore-suspect-keys", "-ig", is_flag=True, default=False,
              help="If True, ignore any keys from CITATION.cff that are likely out of date, such as \'commit\', " +
                   "\'date-released\', \'doi\', and \'version\'.")
@click.option("--verbose", "-v", is_flag=True, default=False, help="Provide feedback on what was entered.")
def cli(infile, outfile, outputformat, url, validate, ignore_suspect_keys, verbose):

    if verbose is True:
        click.echo("{0} = {1}".format("infile", infile))
        click.echo("{0} = {1}".format("outfile", outfile))
        click.echo("{0} = {1}".format("outputformat", outputformat))
        click.echo("{0} = {1}".format("url", url))
        click.echo("{0} = {1}".format("validate", validate))
        click.echo("{0} = {1}".format("ignore_suspect_keys", ignore_suspect_keys))
        click.echo("{0} = {1}".format("verbose", verbose))

    acceptable_output_formats = ["bibtex", "codemeta", "endnote", "ris", "zenodo"]
    if outputformat not in acceptable_output_formats:
        raise ValueError("'--outputformat' should be one of [{0}]".format(", ".join(acceptable_output_formats)))

    if validate:
        # TODO still have to implement validation of the CFF
        print("Still have to implement validation of the CFF")

    if infile is None and url is None:
        infile = "CITATION.cff"
    elif infile is not None and url is not None:
        raise ValueError("You need to specify either \'--infile\' or \'url\' but not both.")

    if infile is None:
        cffstr = None
    else:
        with open(infile, "r") as f:
            cffstr = f.read()

    # TODO currently there is no way to provide values for these 3 arguments
    remove = None
    override = None
    suspect_keys = None

    citation = Citation(url=url, cffstr=cffstr, ignore_suspect_keys=ignore_suspect_keys, override=override,
                        remove=remove, suspect_keys=suspect_keys)
    if outputformat == "bibtex":
        outstr = citation.as_bibtex()
    elif outputformat == "codemeta":
        outstr = citation.as_codemeta()
    elif outputformat == "endnote":
        outstr = citation.as_enw()
    elif outputformat == "ris":
        outstr = citation.as_ris()
    elif outputformat == "zenodo":
        outstr = citation.as_zenodojson()

    if outfile is None:
        print(outstr)
    else:
        with open(outfile, "w") as f:
            f.write(outstr + "\n")
