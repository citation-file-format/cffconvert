# pylint: disable=line-too-long
from cffconvert.cli.rawify_url import rawify_url


def test_github_url_with_owner_repo():
    actual = rawify_url("https://github.com/theownername/thereponame")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/main/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_blob_branchname():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/thebranchname")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/thebranchname/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_blob_branchname_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/thebranchname/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/thebranchname/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_blob_branchname_filename_deep():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/thebranchname/somedir/someotherdir/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/thebranchname/somedir/someotherdir/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_blob_sha():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/0123456789abcdef0123456789abcdef01234567")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_blob_sha_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/0123456789abcdef0123456789abcdef01234567/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_blob_tagname():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/1.0.0")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/1.0.0/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_blob_tagname_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/blob/1.0.0/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/1.0.0/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_commit_sha():
    actual = rawify_url("https://github.com/theownername/thereponame/commit/0123456789abcdef0123456789abcdef01234567")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_commit_sha_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/commit/0123456789abcdef0123456789abcdef01234567/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_tree_branchname():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/thebranchname")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/thebranchname/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_tree_branchname_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/thebranchname/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/thebranchname/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_tree_sha():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/0123456789abcdef0123456789abcdef01234567")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_tree_sha_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/0123456789abcdef0123456789abcdef01234567/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/0123456789abcdef0123456789abcdef01234567/thefilename"
    assert actual == expected


def test_github_url_with_owner_repo_tree_tagname():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/1.0.0")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/1.0.0/CITATION.cff"
    assert actual == expected


def test_github_url_with_owner_repo_tree_tagname_filename():
    actual = rawify_url("https://github.com/theownername/thereponame/tree/1.0.0/thefilename")
    expected = "https://raw.githubusercontent.com/theownername/thereponame/1.0.0/thefilename"
    assert actual == expected
