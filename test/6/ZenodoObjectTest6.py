from cffconvert.ZenodoObject import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml


class ZenodoObjectTest6(unittest.TestCase):

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
                "affiliation": "Netherlands eScience Center",
                "name": "Attema, Jisk"
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Diblen, Faruk",
                "orcid": "0000-0002-0989-929X"
            }
        ]
        self.assertListEqual(zo.creators, expected_creators)

    def test_doi(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_doi()
        self.assertEqual(zo.doi, '10.5281/zenodo.1003346')

    def test_keywords(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_keywords()
        self.assertEqual(zo.keywords, ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data'])

    def test_license(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_license()
        self.assertEqual(zo.license, dict(id='Apache-2.0'))

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
        self.assertEqual(zo.publication_date, '2017-10-07')

    def test_title(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_title()
        self.assertEqual(zo.title, 'spot')

    def test_version(self):
        zo = ZenodoObject(self.cff_object, initialize_empty=True)
        zo.add_version()
        self.assertEqual(zo.version, '0.1.0')
