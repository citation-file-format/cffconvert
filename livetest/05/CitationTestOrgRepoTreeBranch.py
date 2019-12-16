import unittest
from cffconvert import Citation


class CitationTestOrgRepoTreeBranch(unittest.TestCase):

    def test_retrieval_via_branchname(self):
        # https://github.com/<org>/<repo>/tree/<branchname>
        # this test checks if cffconvert can behave similar to a simple curl or wget
        url = "https://github.com/citation-file-format/cff-converter-python/tree/master"
        citation = Citation(url=url)
        self.assertIsNotNone(citation)


if __name__ == "__main__":
    unittest.main()
