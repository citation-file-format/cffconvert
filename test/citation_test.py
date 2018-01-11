import unittest
from citationcff.citation import Citation


class CitationTest(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        self.citation.file_url = "not used in unit testing"
        self.citation.file = """# YAML 1.2
--- 
authors: 
  - 
    affiliation: "Netherlands eScience Center"
    family-names: Kuppevelt
    given-names: Dafne
    name-particle: van
  - 
    affiliation: "Netherlands eScience Center"
    family-names: Meijer
    given-names: Christiaan
  - 
    affiliation: "Netherlands eScience Center"
    family-names: Hees
    given-names: Vincent
    name-particle: van
  - 
    affiliation: "Netherlands eScience Center"
    family-names: Kuzak
    given-names: Mateusz
    orcid: "https://orcid.org/0000-0003-0087-6021"
cff-version: "1.0.3"
commit: 95c5a7f76525655562baeca0af8d334d1796bf57
date-released: 2017-04-06
doi: 10.5281/zenodo.495345
keywords: 
  - "machine learning"
  - "deep learning"
  - "time series"
  - "automatic classification"
license: Apache-2.0
message: "If you use this software, please cite it using these metadata."
repository: "https://github.com/NLeSC/mcfly"
title: mcfly
version: "1.0.1"
"""
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        bibtex_str = self.citation.as_bibtex()
        self.assertEqual("@misc", bibtex_str[:5])

    def test_printing_as_enw(self):
        enw_str = self.citation.as_enw()
        self.assertTrue("%I GitHub repository" in enw_str)


if __name__ == "__main__":
    unittest.main()
