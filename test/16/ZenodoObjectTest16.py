from cffconvert.ZenodoObject import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml


class ZenodoObjectTest16(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            self.cff_object = yaml.safe_load(cffstr)

    def test_creators(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_creators()
        expected_creators = [
            {
                "affiliation": "Springsteen",
                "name": "Van Zandt, Steven"
            },
            {
                "affiliation": "coverband",
                "name": "van Zandt, Steven"
            }
        ]
        self.assertListEqual(zo.creators, expected_creators)

    def test_doi(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_doi()
        self.assertIsNone(zo.doi)

    def test_keywords(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_keywords()
        self.assertIsNone(zo.keywords)

    def test_license(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_license()
        self.assertIsNone(zo.license)

    def test_print(self):
        zo = ZenodoObject(self.cff_object)
        actual_zenodo = zo.print()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodo = f.read()
        self.assertEqual(actual_zenodo, expected_zenodo)

    def test_publication_date(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_publication_date()
        self.assertEqual(zo.publication_date, '2018-01-16')

    def test_title(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_title()
        self.assertEqual(zo.title, 'cff-converter-python')

    def test_version(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_version()
        self.assertEqual(zo.version, '1.0.0')
