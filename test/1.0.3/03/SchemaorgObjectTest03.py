from cffconvert import SchemaorgObject
import unittest
import os
import ruamel.yaml as yaml


class SchemaorgObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.so = SchemaorgObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.so.check_cff_object()
        # doesn't need an assert

    def test_author(self):
        self.so.add_author()
        expected_author = [{
            "@type": "Person",
            "givenName": "Jisk",
            "familyName": "Attema",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            }
        }, {
            "@id": "https://orcid.org/0000-0002-0989-929X",
            "@type": "Person",
            "givenName": "Faruk",
            "familyName": "Diblen",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            }
        }]
        self.assertListEqual(self.so.author, expected_author)

    def test_code_repository(self):
        self.so.add_code_repository()
        self.assertEqual(self.so.code_repository, 'https://github.com/NLeSC/spot')

    def test_date_published(self):
        self.so.add_date_published()
        self.assertEqual(self.so.date_published, '2017-10-07')

    def test_description(self):
        self.so.add_description()
        self.assertIsNone(self.so.description)

    def test_identifier(self):
        self.so.add_identifier()
        self.assertEqual(self.so.identifier, 'https://doi.org/10.5281/zenodo.1003346')

    def test_keywords(self):
        self.so.add_keywords()
        expected_keywords = ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data']
        self.assertListEqual(self.so.keywords, expected_keywords)

    def test_license(self):
        self.so.add_license()
        self.assertEqual(self.so.license, 'https://spdx.org/licenses/Apache-2.0')

    def test_name(self):
        self.so.add_name()
        self.assertEqual(self.so.name, 'spot')

    def test_version(self):
        self.so.add_version()
        self.assertEqual(self.so.version, '0.1.0')

    def test_print(self):
        actual_schemaorg = self.so.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r") as f:
            expected_schemaorg = f.read()
        self.assertEqual(actual_schemaorg, expected_schemaorg)

