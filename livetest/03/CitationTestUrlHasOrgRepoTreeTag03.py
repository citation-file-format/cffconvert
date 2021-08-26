import os
import unittest
from cffconvert import Citation


class CitationTestUrlHasOrgRepoTreeTag(unittest.TestCase):

    def test_retrieval_via_tag(self):
        # https://github.com/<org>/<repo>/tree/<tagname>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/0.0.1"
        citation = Citation(url=url)
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture) as f:
            expected_cffstr = f.read()
        actual_cffstr = citation.cffstr
        self.assertEqual(expected_cffstr, actual_cffstr)


if __name__ == "__main__":
    unittest.main()
