from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml


class BibtexObjectTest3(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.bo = BibtexObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.bo.check_cff_object()
        self.assertTrue(str(context.exception).startswith('\'cff-version\':') and
                        str(context.exception).endswith('isn\'t a supported version.'))

