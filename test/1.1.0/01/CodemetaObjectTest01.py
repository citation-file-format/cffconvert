from cffconvert import CodemetaObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.CodemetaObject import Contract


class CodemetaObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.co = CodemetaObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.co.check_cff_object()
        # doesn't need an assert

    def test_author(self):
        self.co.add_author()
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
        }]
        self.assertListEqual(self.co.author, expected_author)

    def test_code_repository(self):
        self.co.add_code_repository()
        self.assertEqual(self.co.code_repository, 'https://github.com/citation-file-format/cff-converter-python')

    def test_date_published(self):
        self.co.add_date_published()
        self.assertEqual(self.co.date_published, '2018-01-16')

    def test_description(self):
        self.co.add_description()
        self.assertIsNone(self.co.description)

    def test_identifier(self):
        self.co.add_identifier()
        self.assertEqual(self.co.identifier, 'https://doi.org/10.5281/zenodo.1162057')

    def test_keywords(self):
        self.co.add_keywords()
        expected_keywords = ['citation', 'bibliography', 'cff', 'CITATION.cff']
        self.assertListEqual(self.co.keywords, expected_keywords)

    def test_license(self):
        self.co.add_license()
        self.assertEqual(self.co.license, 'https://spdx.org/licenses/Apache-2.0')

    def test_name(self):
        self.co.add_name()
        self.assertEqual(self.co.name, 'cff-converter-python')

    def test_version(self):
        self.co.add_version()
        self.assertEqual(self.co.version, '1.0.0')

    def test_print(self):
        actual_codemeta = self.co.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "r", encoding="utf8") as f:
            expected_codemeta = f.read()
        self.assertEqual(actual_codemeta, expected_codemeta)

