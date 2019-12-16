from cffconvert.CodemetaObject import CodemetaObject
import unittest
import os
import ruamel.yaml as yaml


class CodemetaObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
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
        self.assertListEqual(self.co.author, expected_author)

    def test_code_repository(self):
        self.co.add_code_repository()
        self.assertEqual(self.co.code_repository, 'https://github.com/NLeSC/spot')

    def test_date_published(self):
        self.co.add_date_published()
        self.assertEqual(self.co.date_published, '2017-10-07')

    def test_description(self):
        self.co.add_description()
        self.assertIsNone(self.co.description)

    def test_identifier(self):
        self.co.add_identifier()
        self.assertEqual(self.co.identifier, 'https://doi.org/10.5281/zenodo.1003346')

    def test_keywords(self):
        self.co.add_keywords()
        expected_keywords = ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data']
        self.assertListEqual(self.co.keywords, expected_keywords)

    def test_license(self):
        self.co.add_license()
        self.assertEqual(self.co.license, 'https://spdx.org/licenses/Apache-2.0')

    def test_name(self):
        self.co.add_name()
        self.assertEqual(self.co.name, 'spot')

    def test_version(self):
        self.co.add_version()
        self.assertEqual(self.co.version, '0.1.0')

    def test_print(self):
        actual_codemeta = self.co.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        self.assertEqual(actual_codemeta, expected_codemeta)

