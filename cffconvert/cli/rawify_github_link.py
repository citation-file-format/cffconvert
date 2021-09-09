def rawify_github_link(url):
    # just a placeholder replacement for the moment
    if url == "https://github.com/citation-file-format/cff-converter-python":
        return "https://raw.githubusercontent.com/citation-file-format/cff-converter-python/main/CITATION.cff"
    # return unrecognized URLs as-is
    return url
