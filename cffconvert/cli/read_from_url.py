import requests
from cffconvert.cli.rawify_github_link import rawify_github_link


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")

    url_fetch = rawify_github_link(url)

    r = requests.get(url_fetch)
    if r.ok:
        return r.text
    raise Exception("Error while trying to retrieve {0}".format(url_fetch))
