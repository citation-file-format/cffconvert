from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml


class BibtexObjectTest1(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.bo = BibtexObject(cff_object, initialize_empty=True)

    def test_author(self):
        self.bo.add_author()
        self.assertTrue(self.bo.author == 'author = {Gonzalo Fernández de Córdoba Jr.}')

    def test_check_cff_object(self):
        self.bo.check_cff_object()
        # doesn't need an assert

    def test_doi(self):
        self.bo.add_doi()
        self.assertIsNone(self.bo.doi)

    def test_month(self):
        self.bo.add_month()
        self.assertIsNone(self.bo.month)

    def test_print(self):
        actual_bibtex = self.bo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        self.assertEqual(actual_bibtex, expected_bibtex)

    def test_title(self):
        self.bo.add_title()
        self.assertTrue(self.bo.title == 'title = {example title}')

    def test_url(self):
        self.bo.add_url()
        self.assertIsNone(self.bo.url)

    def test_year(self):
        self.bo.add_year()
        self.assertIsNone(self.bo.year)

