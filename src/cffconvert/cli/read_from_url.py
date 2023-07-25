import os
import requests
from cffconvert.cli.rawify_url import rawify_url as rawify
from cffconvert.cli.constants import github_api_version_header


def read_from_url(url):
    if not url.startswith("https://"):
        raise AssertionError("URL should be an https:// link")
    url_raw = rawify(url)
    headers = github_api_version_header
    headers.update({"Accept": "text/plain"})
    token = os.environ.get("CFFCONVERT_GITHUB_API_TOKEN")
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
