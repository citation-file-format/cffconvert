from cffconvert.SchemaorgObject import SchemaorgObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.SchemaorgObject import Contract


class SchemaorgObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.so = SchemaorgObject(cff_object, initialize_empty=True)

    def test_author(self):
        pass

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.so.check_cff_object()
        self.assertTrue(str(context.exception).startswith('\'cff-version\':') and
                        str(context.exception).endswith('isn\'t a supported version.'))

    def test_code_repository(self):
        pass

    def test_date_published(self):
        pass

    def test_description(self):
        pass

    def test_identifier(self):
        pass

    def test_keywords(self):
        pass

    def test_license(self):
        pass

    def test_name(self):
        pass

    def test_version(self):
        pass

    def test_print(self):
        pass
