from cffconvert.ZenodoObject import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml


class ZenodoObjectTest6(unittest.TestCase):

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
                "affiliation": "Netherlands eScience Center",
                "name": "Attema, Jisk"
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Diblen, Faruk",
                "orcid": "0000-0002-0989-929X"
            }
        ]
        self.assertListEqual(self.zo.creators, expected_creators)

    def test_doi(self):
        self.zo.add_doi()
        self.assertEqual(self.zo.doi, '10.5281/zenodo.1003346')

    def test_keywords(self):
        self.zo.add_keywords()
        self.assertEqual(self.zo.keywords, ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data'])

    def test_license(self):
        self.zo.add_license()
        self.assertEqual(self.zo.license, dict(id='Apache-2.0'))

    def test_print(self):
        actual_zenodo = self.zo.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodo = f.read()
        self.assertEqual(actual_zenodo, expected_zenodo)

    def test_publication_date(self):
        self.zo.add_publication_date()
        self.assertEqual(self.zo.publication_date, '2017-10-07')

    def test_title(self):
        self.zo.add_title()
        self.assertEqual(self.zo.title, 'spot')

    def test_version(self):
        self.zo.add_version()
        self.assertEqual(self.zo.version, '0.1.0')
