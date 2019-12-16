from cffconvert.CodemetaObject import CodemetaObject
import unittest
import os
import ruamel.yaml as yaml


class CodemetaObjectTest02(unittest.TestCase):

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
            "givenName": "Gonzalo",
            "familyName": "Fernández de Córdoba Jr.",
        }]
        self.assertListEqual(self.co.author, expected_author)

    def test_code_repository(self):
        self.co.add_code_repository()
        self.assertIsNone(self.co.code_repository)

    def test_date_published(self):
        self.co.add_date_published()
        self.assertIsNone(self.co.date_published)

    def test_description(self):
        self.co.add_description()
        self.assertIsNone(self.co.description)

    def test_identifier(self):
        self.co.add_identifier()
        self.assertIsNone(self.co.identifier)

    def test_keywords(self):
        self.co.add_keywords()
        self.assertIsNone(self.co.keywords)

    def test_license(self):
        self.co.add_license()
        self.assertIsNone(self.co.license)

    def test_name(self):
        self.co.add_name()
        self.assertEqual(self.co.name, 'example title')

    def test_version(self):
        self.co.add_version()
        self.assertEqual(self.co.version, '1.0.0')

    def test_print(self):
        actual_codemeta = self.co.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        self.assertEqual(actual_codemeta, expected_codemeta)

