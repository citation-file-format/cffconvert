from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml


class BibtexObjectTest6(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            self.cff_object = yaml.safe_load(cffstr)

    def test_author(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_author()
        self.assertTrue(bo.author == 'author = {Jisk Attema and Faruk Diblen}')

    def test_doi(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_doi()
        self.assertTrue(bo.doi == 'doi = {10.5281/zenodo.1003346}')

    def test_month(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_month()
        self.assertTrue(bo.month == 'month = {10}')

    def test_print(self):
        bo = BibtexObject(self.cff_object)
        actual_bibtex = bo.print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        self.assertEqual(actual_bibtex, expected_bibtex)

    def test_title(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_title()
        self.assertTrue(bo.title == 'title = {spot}')

    def test_url(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_url()
        self.assertTrue(bo.url == 'url = {https://github.com/NLeSC/spot}')

    def test_year(self):
        bo = BibtexObject(self.cff_object, initialize_empty=True)
        bo.add_year()
        self.assertTrue(bo.year == 'year = {2017}')
