import os
from tests.contracts.apalike_object import Contract
from cffconvert import Citation
from cffconvert.behavior_1_0_x.apalike_object import ApalikeObject


def apalike_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ApalikeObject(citation.cffobj, initialize_empty=True)


class TestApalikeObject(Contract):

    def test_as_string(self):
        actual_apalike = apalike_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "apalike.txt")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_apalike = f.read()
        assert actual_apalike == expected_apalike

    def test_author(self):
        assert apalike_object().add_author().author == 'Fernández de Córdoba Jr. G.'

    def test_check_cffobj(self):
        apalike_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert apalike_object().add_doi().doi is None

    def test_title(self):
        assert apalike_object().add_title().title == 'example title'

    def test_url(self):
        assert apalike_object().add_url().url is None

    def test_version(self):
        assert apalike_object().add_version().version == '(version 1.0.0).'

    def test_year(self):
        assert apalike_object().add_year().year == '(1999).'