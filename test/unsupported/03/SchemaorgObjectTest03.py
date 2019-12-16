from cffconvert.SchemaorgObject import SchemaorgObject
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
        with self.assertRaises(ValueError) as context:
            self.so.check_cff_object()
        self.assertTrue('Missing key "cff-version" in CITATION.cff file.' in str(context.exception))
