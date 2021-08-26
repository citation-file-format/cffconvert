import os
import unittest
from test.contracts.BibtexObject import Contract
import ruamel.yaml as yaml
from cffconvert import BibtexObject


class BibtexObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.bo = BibtexObject(cff_object, initialize_empty=True)

    def test_author(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.bo.check_cff_object()
        self.assertTrue('Missing key "cff-version" in CITATION.cff file.' in str(context.exception))

    def test_doi(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_month(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_print(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_title(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_url(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_year(self):
        # CFF file is not valid, hence contract does not apply
        pass
