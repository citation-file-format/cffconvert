from cffconvert import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.ZenodoObject import Contract


class ZenodoObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.zo = ZenodoObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.zo.check_cff_object()
        # doesn't need an assert

    def test_creators(self):
        self.zo.add_creators()
        expected_creators = [
            {
                "name": "Fernández de Córdoba Jr., Gonzalo"
            }
        ]
        self.assertListEqual(self.zo.creators, expected_creators)

    def test_doi(self):
        self.zo.add_doi()
        self.assertIsNone(self.zo.doi)

    def test_keywords(self):
        self.zo.add_keywords()
        self.assertIsNone(self.zo.keywords)

    def test_license(self):
        self.zo.add_license()
        self.assertIsNone(self.zo.license)

    def test_print(self):
        actual_zenodo = self.zo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodo = f.read()
        self.assertEqual(actual_zenodo, expected_zenodo)

    def test_publication_date(self):
        self.zo.add_publication_date()
        self.assertIsNone(self.zo.publication_date)

    def test_title(self):
        self.zo.add_title()
        self.assertEqual(self.zo.title, 'example title')

    def test_version(self):
        self.zo.add_version()
        self.assertEqual(self.zo.version, '1.0.0')
