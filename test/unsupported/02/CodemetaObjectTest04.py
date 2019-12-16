from cffconvert.CodemetaObject import CodemetaObject
import unittest
import os
import ruamel.yaml as yaml


class CodemetaObjectTest04(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.co = CodemetaObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.co.check_cff_object()
        self.assertTrue('Expected cff_object to be of type \'dict\'.' in str(context.exception))
