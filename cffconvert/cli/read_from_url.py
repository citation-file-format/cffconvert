import requests
from cffconvert.cli.rawify_url import rawify_url as rawify


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")

    url_raw = rawify(url)

    r = requests.get(url_raw)
    if r.ok:
        return r.text
    raise Exception("Error while trying to retrieve {0}".format(url_raw))
