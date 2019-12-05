from cffconvert.ZenodoObject import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml


class ZenodoObjectTest12(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            self.cff_object = yaml.safe_load(cffstr)

    def test_creators(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_creators()
        expected_creators = [
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Spaaks, Jurriaan H."
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Klaver, Tom"
            }
        ]
        self.assertListEqual(zo.creators, expected_creators)

    def test_doi(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_doi()
        self.assertEqual(zo.doi, '10.5281/zenodo.1162057')

    def test_keywords(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_keywords()
        self.assertEqual(zo.keywords, ['citation', 'bibliography', 'cff', 'CITATION.cff'])

    def test_license(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_license()
        self.assertEqual(zo.license, dict(id='Apache-2.0'))

    def test_publication_date(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_publication_date()
        self.assertEqual(zo.publication_date, '2018-01-16')

    def test_title(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_title()
        self.assertEqual(zo.title, 'cff-converter-python')

    def test_version(self):
        zo = ZenodoObject(self.cff_object)
        zo.add_version()
        self.assertEqual(zo.version, '1.0.0')
