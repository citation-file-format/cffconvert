from cffconvert import RisObject
import unittest
import os
import ruamel.yaml as yaml


class RisObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.ro = RisObject(cff_object, initialize_empty=True)

    def test_abstract(self):
        self.ro.add_abstract()
        self.assertIsNone(self.ro.abstract)

    def test_author(self):
        self.ro.add_author()
        self.assertEqual(self.ro.author, 'AU  - Spaaks, Jurriaan H.\nAU  - Klaver, Tom\n')

    def test_check_cff_object(self):
        self.ro.check_cff_object()
        # doesn't need an assert

    def test_date(self):
        self.ro.add_date()
        self.assertEqual(self.ro.date, 'DA  - 2018-01-16\n')

    def test_doi(self):
        self.ro.add_doi()
        self.assertEqual(self.ro.doi, 'DO  - 10.5281/zenodo.1162057\n')

    def test_keywords(self):
        self.ro.add_keywords()
        self.assertEqual(self.ro.keywords, 'KW  - citation\nKW  - bibliography\nKW  - cff\nKW  - CITATION.cff\n')

    def test_print(self):
        actual_ris = self.ro.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        self.assertEqual(actual_ris, expected_ris)

    def test_title(self):
        self.ro.add_title()
        self.assertEqual(self.ro.title, 'TI  - cff-converter-python\n')

    def test_url(self):
        self.ro.add_url()
        self.assertEqual(self.ro.url, 'UR  - https://github.com/citation-file-format/cff-converter-python\n')

    def test_year(self):
        self.ro.add_year()
        self.assertEqual(self.ro.year, 'PY  - 2018\n')

