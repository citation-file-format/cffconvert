import unittest
import os
from citationcff.citation import Citation


class CitationTest(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "citation-mcfly-1")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        bibtex_str = self.citation.as_bibtex()
        self.assertEqual("@misc", bibtex_str[:5])

    def test_printing_as_enw(self):
        enw_str = self.citation.as_enw()
        self.assertTrue("%I GitHub repository" in enw_str)


if __name__ == "__main__":
    unittest.main()
