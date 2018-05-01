import click
from cffconvert import Citation


@click.command()
@click.argument("url", type=click.STRING)
@click.argument("outputfilename", type=click.Path())
@click.argument("outputformat")
@click.option("--validate", default=False, help="Validate the CITATION.cff found at the URL")
def cli(url, outputfilename, outputformat, validate):

    acceptable_output_formats = ["bibtex", "codemeta", "endnote", "ris", "zenodo"]
    if outputformat not in acceptable_output_formats:
        raise ValueError("\'OUTPUTFORMAT should be one of [{0}]".format(", ".join(acceptable_output_formats)))

    if validate:
        # still have to implement validation of the CFF
        pass

    if url is not None:
        if outputformat == "bibtex":
            citation = Citation(url).as_bibtex()
        elif outputformat == "codemeta":
            citation = Citation(url).as_codemeta()
        elif outputformat == "endnote":
            citation = Citation(url).as_enw()
        elif outputformat == "ris":
            citation = Citation(url).as_ris()
        elif outputformat == "zenodo":
            citation = Citation(url).as_zenodojson()

        with open(outputfilename, "w") as f:
            f.write(citation)
