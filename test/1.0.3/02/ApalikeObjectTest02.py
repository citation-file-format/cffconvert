import os
import unittest
from test.contracts.ApalikeObject import Contract
import ruamel.yaml as yaml
from cffconvert import ApalikeObject


class ApalikeObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.ao = ApalikeObject(cff_object, initialize_empty=True)

    def test_author(self):
        self.ao.add_author()
        self.assertEqual(self.ao.author, 'Fernández de Córdoba Jr. G.')

    def test_check_cff_object(self):
        self.ao.check_cff_object()
        # doesn't need an assert

    def test_year(self):
        self.ao.add_year()
        self.assertEqual(self.ao.year, ' (1999). ')

    def test_title(self):
        self.ao.add_title()
        self.assertEqual(self.ao.title, 'example title')

    def test_version(self):
        self.ao.add_version()
        self.assertEqual(self.ao.version, ' (version 1.0.0). ')

    def test_doi(self):
        self.ao.add_doi()
        self.assertIsNone(self.ao.doi)

    def test_url(self):
        self.ao.add_url()
        self.assertIsNone(self.ao.url)
