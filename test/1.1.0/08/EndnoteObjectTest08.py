from cffconvert.EndnoteObject import EndnoteObject
import unittest
import os
import ruamel.yaml as yaml


class EndnoteObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.eo = EndnoteObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.eo.check_cff_object()
        # doesn't need an assert

    def test_author(self):
        self.eo.add_author()
        self.assertEqual(self.eo.author, '%A Van Zandt, Steven\n%A van Zandt, Steven\n')

    def test_doi(self):
        self.eo.add_doi()
        self.assertIsNone(self.eo.doi)

    def test_keyword(self):
        self.eo.add_keyword()
        self.assertIsNone(self.eo.keyword)

    def test_name(self):
        self.eo.add_name()
        self.assertEqual(self.eo.name, '%T cff-converter-python\n')

    def test_print(self):
        actual_endnote = self.eo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        self.assertEqual(actual_endnote, expected_endnote)

    def test_url(self):
        self.eo.add_url()
        self.assertIsNone(self.eo.url)

    def test_year(self):
        self.eo.add_year()
        self.assertEqual(self.eo.year, '%D 2018\n')

