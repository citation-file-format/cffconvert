import os
import requests
from cffconvert.cli.constants import GITHUB_API_VERSION_HEADER
from cffconvert.cli.rawify_url import rawify_url as rawify


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")
    url_raw = rawify(url)
    headers = GITHUB_API_VERSION_HEADER
    headers.update({"Accept": "text/plain"})
    token = os.environ.get("CFFCONVERT_API_TOKEN")
    if token is None:
        # Proceed with making the call without authenticating -- stricter rate limits apply
        pass
    else:
        headers.update({"Authorization": f"Bearer { token }"})
    response = requests.get(url_raw, headers=headers, timeout=30)
    if response.ok:
        return response.text
    print(f"Error while trying to retrieve {url_raw}")
    response.raise_for_status()
    return None
