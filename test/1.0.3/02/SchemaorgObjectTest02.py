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
            "givenName": "Gonzalo",
            "familyName": "Fernández de Córdoba Jr.",
        }]
        self.assertListEqual(self.so.author, expected_author)

    def test_code_repository(self):
        self.so.add_code_repository()
        self.assertIsNone(self.so.code_repository)

    def test_date_published(self):
        self.so.add_date_published()
        self.assertIsNone(self.so.date_published)

    def test_description(self):
        self.so.add_description()
        self.assertIsNone(self.so.description)

    def test_identifier(self):
        self.so.add_identifier()
        self.assertIsNone(self.so.identifier)

    def test_keywords(self):
        self.so.add_keywords()
        self.assertIsNone(self.so.keywords)

    def test_license(self):
        self.so.add_license()
        self.assertIsNone(self.so.license)

    def test_name(self):
        self.so.add_name()
        self.assertEqual(self.so.name, 'example title')

    def test_version(self):
        self.so.add_version()
        self.assertEqual(self.so.version, '1.0.0')

    def test_print(self):
        actual_schemaorg = self.so.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r") as f:
            expected_schemaorg = f.read()
        self.assertEqual(actual_schemaorg, expected_schemaorg)

