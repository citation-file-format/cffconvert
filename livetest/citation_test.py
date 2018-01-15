import unittest
import os
from citationcff.citation import Citation


class CitationTest(unittest.TestCase):

    def setUp(self):
        url = "https://github.com/jspaaks/trellis"
        self.citation = Citation(url)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "mcfly-bibtex-1")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "mcfly-endnote-1")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "mcfly-ris-1")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


if __name__ == "__main__":
    unittest.main()
