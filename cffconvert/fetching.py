import requests


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")

    url_fetch = rawify_github_link(url)

    r = requests.get(url_fetch)
    if r.ok:
        return r.text
    else:
        raise Exception("Error while trying to retrieve {0}".format(url_fetch))


def rawify_github_link(url):
    # just a placeholder replacement for the moment
    if url == "https://github.com/citation-file-format/cff-converter-python":
        return "https://raw.githubusercontent.com/citation-file-format/cff-converter-python/main/CITATION.cff"
    # return unrecognized URLs as-is
    return url
