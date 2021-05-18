from cffconvert import BibtexObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.BibtexObject import Contract


class BibtexObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.bo = BibtexObject(cff_object, initialize_empty=True)

    def test_author(self):
        self.bo.add_author()
        self.assertEqual(self.bo.author, 'author = {Jurriaan H. Spaaks and Tom Klaver' +
                                         ' and Stefan Verhoeven and Stephan Druskat}')

    def test_check_cff_object(self):
        self.bo.check_cff_object()
        # doesn't need an assert

    def test_doi(self):
        self.bo.add_doi()
        self.assertEqual(self.bo.doi, 'doi = {10.5281/zenodo.1162057}')

    def test_month(self):
        self.bo.add_month()
        self.assertEqual(self.bo.month, 'month = {7}')

    def test_print(self):
        actual_bibtex = self.bo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "r", encoding="utf8") as f:
            expected_bibtex = f.read()
        self.assertEqual(actual_bibtex, expected_bibtex)

    def test_title(self):
        self.bo.add_title()
        self.assertEqual(self.bo.title, 'title = {cffconvert}')

    def test_url(self):
        self.bo.add_url()
        self.assertEqual(self.bo.url, 'url = {https://github.com/citation-file-format/cff-converter-python}')

    def test_year(self):
        self.bo.add_year()
        self.assertEqual(self.bo.year, 'year = {2018}')
