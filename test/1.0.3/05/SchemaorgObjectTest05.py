import os
import unittest
from test.contracts.SchemaorgObject import Contract
import ruamel.yaml as yaml
from cffconvert import SchemaorgObject


class SchemaorgObjectTest(Contract, unittest.TestCase):

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
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Spaaks",
            "givenName": "Jurriaan H."
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Klaver",
            "givenName": "Tom"
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Verhoeven",
            "givenName": "Stefan"
        }]
        self.assertListEqual(self.so.author, expected_author)

    def test_code_repository(self):
        self.so.add_code_repository()
        self.assertEqual(self.so.code_repository, 'https://github.com/citation-file-format/cff-converter-python')

    def test_date_published(self):
        self.so.add_date_published()
        self.assertEqual(self.so.date_published, '2018-05-09')

    def test_description(self):
        self.so.add_description()
        self.assertIsNone(self.so.description)

    def test_identifier(self):
        self.so.add_identifier()
        self.assertEqual(self.so.identifier, 'https://doi.org/10.5281/zenodo.1162057')

    def test_keywords(self):
        self.so.add_keywords()
        expected_keywords = ['citation', 'bibliography', 'cff', 'CITATION.cff']
        self.assertListEqual(self.so.keywords, expected_keywords)

    def test_license(self):
        self.so.add_license()
        self.assertEqual(self.so.license, 'https://spdx.org/licenses/Apache-2.0')

    def test_name(self):
        self.so.add_name()
        self.assertEqual(self.so.name, 'cffconvert')

    def test_version(self):
        self.so.add_version()
        self.assertEqual(self.so.version, '0.0.4')

    def test_print(self):
        actual_schemaorg = self.so.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r") as f:
            expected_schemaorg = f.read()
        self.assertEqual(actual_schemaorg, expected_schemaorg)
