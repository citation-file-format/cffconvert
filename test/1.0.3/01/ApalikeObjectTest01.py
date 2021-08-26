import os
import unittest
from test.contracts.ApalikeObject import Contract
import ruamel.yaml as yaml
from cffconvert import ApalikeObject


class ApalikeObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.ao = ApalikeObject(cff_object, initialize_empty=True)

    def test_author(self):
        self.ao.add_author()
        self.assertEqual(self.ao.author, 'Spaaks J.H., Klaver T.')

    def test_check_cff_object(self):
        self.ao.check_cff_object()
        # doesn't need an assert

    def test_year(self):
        self.ao.add_year()
        self.assertEqual(self.ao.year, ' (2018). ')

    def test_title(self):
        self.ao.add_title()
        self.assertEqual(self.ao.title, 'cff-converter-python')

    def test_version(self):
        self.ao.add_version()
        self.assertEqual(self.ao.version, ' (version 1.0.0). ')

    def test_doi(self):
        self.ao.add_doi()
        self.assertEqual(self.ao.doi, 'DOI: http://doi.org/10.5281/zenodo.1162057 ')

    def test_url(self):
        self.ao.add_url()
        self.assertEqual(self.ao.url, 'URL: https://github.com/citation-file-format/cff-converter-python\n')
