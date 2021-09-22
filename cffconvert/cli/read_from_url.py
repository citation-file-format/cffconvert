import requests
from cffconvert.cli.rawify_url import rawify_url as rawify


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")

    url_raw = rawify(url)

    response = requests.get(url_raw)
    if response.ok:
        return response.text
    print(f"Error while trying to retrieve {url_raw}")
    response.raise_for_status()
    return None
