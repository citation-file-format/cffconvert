from cffconvert import EndnoteObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.EndnoteObject import Contract


class EndnoteObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.eo = EndnoteObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.eo.check_cff_object()
        # doesn't need an assert

    def test_author(self):
        self.eo.add_author()
        self.assertEqual(self.eo.author, '%A Attema, Jisk\n%A Diblen, Faruk\n')

    def test_doi(self):
        self.eo.add_doi()
        self.assertEqual(self.eo.doi, '%R 10.5281/zenodo.1003346\n')

    def test_keyword(self):
        self.eo.add_keyword()
        self.assertEqual(self.eo.keyword, '%K visualization\n%K big data\n%K visual ' + \
                                          'data analytics\n%K multi-dimensional data\n')

    def test_name(self):
        self.eo.add_name()
        self.assertEqual(self.eo.name, '%T spot\n')

    def test_print(self):
        actual_endnote = self.eo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "r", encoding="utf8") as f:
            expected_endnote = f.read()
        self.assertEqual(actual_endnote, expected_endnote)

    def test_url(self):
        self.eo.add_url()
        self.assertEqual(self.eo.url, '%U https://github.com/NLeSC/spot\n')

    def test_year(self):
        self.eo.add_year()
        self.assertEqual(self.eo.year, '%D 2017\n')

