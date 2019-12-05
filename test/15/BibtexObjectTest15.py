from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml


class BibtexObjectTest15(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            self.cff_object = yaml.safe_load(cffstr)

    def test_author(self):
        bo = BibtexObject(self.cff_object)
        bo.add_author()
        self.assertTrue(bo.author == 'author = {Jurriaan H. Spaaks and Tom Klaver and mysteryauthor}\n')

    def test_doi(self):
        bo = BibtexObject(self.cff_object)
        bo.add_doi()
        self.assertTrue(bo.doi == 'doi = {10.5281/zenodo.1162057}\n')

    def test_month(self):
        bo = BibtexObject(self.cff_object)
        bo.add_month()
        self.assertTrue(bo.month == 'month = {1}\n')

    def test_title(self):
        bo = BibtexObject(self.cff_object)
        bo.add_title()
        self.assertTrue(bo.title == 'title = {cff-converter-python}\n')

    def test_url(self):
        bo = BibtexObject(self.cff_object)
        bo.add_url()
        self.assertTrue(bo.url == 'url = {https://github.com/citation-file-format/cff-converter-python}\n')

    def test_year(self):
        bo = BibtexObject(self.cff_object)
        bo.add_year()
        self.assertTrue(bo.year == 'year = {2018}\n')

