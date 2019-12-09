from cffconvert.SchemaorgObject import SchemaorgObject
import unittest
import os
import ruamel.yaml as yaml


class SchemaorgObjectTest1(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.so = SchemaorgObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.so.check_cff_object()
        # doesn't need an assert

    def test_code_repository(self):
        self.so.add_code_repository()
        self.assertEqual(self.so.code_repository, 'https://github.com/citation-file-format/cff-converter-python')

    def test_print(self):
        actual_schemaorg = self.so.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r") as f:
            expected_schemaorg = f.read()
        self.assertEqual(actual_schemaorg, expected_schemaorg)

