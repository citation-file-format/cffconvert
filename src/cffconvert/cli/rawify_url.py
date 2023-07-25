import os
import requests
from cffconvert.cli.constants import github_api_version_header


def rawify_url(url):
    if url.startswith("https://github.com"):
        urlparts = url.replace("https://github.com", "", 1).strip("/").split("/") + [None] * 5
        ownername, reponame, _, refvalue, *filename_parts = urlparts
        filename = "/".join([p for p in filename_parts if p is not None])
        assert ownername is not None, "URL should include the name of the owner/organization."
        assert reponame is not None, "URL should include the name of the repository."
        if refvalue is None:
            default_branch = None
            try:
                repos_api = f"https://api.github.com/repos/{ownername}/{reponame}"
                headers = github_api_version_header
                headers.update({"Accept": "application/vnd.github+json"})
                token = os.environ.get("CFFCONVERT_GITHUB_API_TOKEN")
                if token is None:
                    # Proceed with making the call without authenticating -- stricter rate limits apply
                    pass
                else:
                    headers.update({"Authorization": f"Bearer { token }"})
                response = requests.get(repos_api, headers=headers, timeout=10)
                if response.ok:
                    default_branch = response.json().get("default_branch")
            finally:
                refvalue = default_branch or "main"
        if filename == "":
            filename = "CITATION.cff"
        return f"https://raw.githubusercontent.com/{ownername}/{reponame}/{refvalue}/{filename}"

    # return unrecognized URLs as-is
    return url
