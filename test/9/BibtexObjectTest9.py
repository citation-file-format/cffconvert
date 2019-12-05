from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml


class BibtexObjectTest9(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            self.cff_object = yaml.safe_load(cffstr)

    def test_author(self):
        bo = BibtexObject(self.cff_object)
        bo.add_author()
        self.assertTrue(bo.author == 'author = {Jurriaan H. Spaaks and Tom Klaver}')

    def test_doi(self):
        bo = BibtexObject(self.cff_object)
        bo.add_doi()
        self.assertTrue(bo.doi == 'doi = {10.5281/zenodo.1162057}')

    def test_month(self):
        bo = BibtexObject(self.cff_object)
        bo.add_month()
        self.assertTrue(bo.month == 'month = {1}')

    def test_title(self):
        bo = BibtexObject(self.cff_object)
        bo.add_title()
        self.assertTrue(bo.title == 'title = {cff-converter-python}')

    def test_url(self):
        bo = BibtexObject(self.cff_object)
        bo.add_url()
        self.assertTrue(bo.url == 'url = {https://github.com/citation-file-format/cff-converter-python}')

    def test_year(self):
        bo = BibtexObject(self.cff_object)
        bo.add_year()
        self.assertTrue(bo.year == 'year = {2018}')

    def test_print(self):
        bo = BibtexObject(self.cff_object)
        actual_bibtex = bo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        self.assertEqual(actual_bibtex, expected_bibtex)

