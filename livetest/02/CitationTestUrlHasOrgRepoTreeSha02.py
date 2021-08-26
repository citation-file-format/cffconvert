import os
import unittest
from cffconvert import Citation


class CitationTestUrlHasOrgRepoTreeSha(unittest.TestCase):

    def test_retrieval_via_sha(self):
        # https://github.com/<org>/<repo>/tree/<sha>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/" + \
              "b7505591cf421ab33156ec0bffb0af43fd7d2cd1"
        citation = Citation(url=url)
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture) as f:
            expected_cffstr = f.read()
        actual_cffstr = citation.cffstr
        self.assertEqual(expected_cffstr, actual_cffstr)


if __name__ == "__main__":
    unittest.main()
