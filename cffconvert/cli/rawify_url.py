def rawify_url(url):
    github_base_url = "https://github.com"
    if url.startswith(github_base_url):
        n = len("https://github.com") + 1
        ownername, reponame, reftype, refvalue, filename = (url[n:].split('/') + [None] * 3)[:5]
        if refvalue is None:
            refvalue = "main"
        if filename is None:
            filename = "CITATION.cff"
        return "https://raw.githubusercontent.com/{0}/{1}/{2}/{3}".format(ownername, reponame, refvalue, filename)

    # return unrecognized URLs as-is
    return url
