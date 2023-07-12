from cffconvert.citation import Citation
from cffconvert.cli.read_from_file import read_from_file
from cffconvert.cli.read_from_url import read_from_url


def create_citation(infile, url):
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
        cffstr = read_from_file(infile)
        return Citation(cffstr, src=infile)

    raise ValueError("Something went wrong creating the citation object.")
