def rawify_url(url):
    if url.startswith("https://github.com"):
        n = len("https://github.com")
        urlparts = (url[n:].strip('/').split('/') + [None] * 5)
        ownername, reponame, _, refvalue, *filename_parts = urlparts
        filename = '/'.join([p for p in filename_parts if p is not None])
        assert ownername is not None, "URL should include the name of the owner/organization."
        assert reponame is not None, "URL should include the name of the repository."
        if refvalue is None:
            refvalue = "main"
        if filename is None or filename == '':
            filename = "CITATION.cff"
        return "https://raw.githubusercontent.com/{0}/{1}/{2}/{3}".format(ownername, reponame, refvalue, filename)

    # return unrecognized URLs as-is
    return url
