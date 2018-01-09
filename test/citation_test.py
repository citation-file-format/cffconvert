import unittest
from citationcff.citation import Citation


class CitationTest(unittest.TestCase):

    def setUp(self):
        url = "https://github.com/jspaaks/trellis"
        self.citation = Citation(url, instantiate_empty=True)

    def test_retrieving_a_url(self):
        self.assertTrue(self.citation.file is None)
        self.citation._retrieve_file()
        self.assertFalse(self.citation.file is None)

    def test_parsing_yaml(self):
        self.citation._retrieve_file()
        self.assertTrue(self.citation.as_yaml is None)
        self.citation._parse_yaml()
        self.assertFalse(self.citation.as_yaml is None)

    def test_printing_as_bibtex(self):
        self.citation._retrieve_file()
        self.citation._parse_yaml()
        bibtex_str = self.citation.as_bibtex()
        self.assertEqual("@misc", bibtex_str[:5])


if __name__ == "__main__":
    unittest.main()
