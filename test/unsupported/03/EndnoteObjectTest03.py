import os
import unittest
from test.contracts.EndnoteObject import Contract
import ruamel.yaml as yaml
from cffconvert import EndnoteObject


class EndnoteObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.eo = EndnoteObject(cff_object, initialize_empty=True)

    def test_author(self):
        pass

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.eo.check_cff_object()
        self.assertTrue('Missing key "cff-version" in CITATION.cff file.' in str(context.exception))

    def test_doi(self):
        pass

    def test_keyword(self):
        pass

    def test_name(self):
        pass

    def test_print(self):
        pass

    def test_url(self):
        pass

    def test_year(self):
        pass
