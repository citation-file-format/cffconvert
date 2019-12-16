from cffconvert.EndnoteObject import EndnoteObject
import unittest
import os
import ruamel.yaml as yaml


class EndnoteObjectTest(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.eo = EndnoteObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        self.eo.check_cff_object()
        # doesn't need an assert

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.eo.check_cff_object()
        self.assertTrue(str(context.exception).startswith('\'cff-version\':') and
                        str(context.exception).endswith('isn\'t a supported version.'))
