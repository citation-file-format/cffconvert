import unittest
from cffconvert import Citation


class CitationTestUrlHasOrgRepoOnly(unittest.TestCase):

    def test_retrieval_of_latest_master(self):
        # this test checks if cffconvert can behave similar to a simple curl or wget
        # https://github.com/<org>/<repo>
        url = "https://github.com/citation-file-format/cff-converter-python"
        citation = Citation(url=url)
        self.assertIsNotNone(citation)


if __name__ == "__main__":
    unittest.main()
