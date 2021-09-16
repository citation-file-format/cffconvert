import os
import pytest
from test.contracts.apalike_object import Contract
from cffconvert.behavior_1_2_x.apalike_object import ApalikeObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def apalike_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ApalikeObject(citation.cffobj, initialize_empty=True)


class TestApalikeObject(Contract):

    def test_as_string(self, apalike_object):
        actual_apalike = apalike_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "apalike.txt")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_apalike = f.read()
        assert actual_apalike == expected_apalike

    def test_author(self, apalike_object):
        assert apalike_object.add_author().author == 'Spaaks J.H., Klaver T.'

    def test_check_cffobj(self, apalike_object):
        apalike_object.check_cffobj()
        # doesn't need an assert

    def test_doi(self, apalike_object):
        assert apalike_object.add_doi().doi == 'DOI: 10.5281/zenodo.1162057'

    def test_title(self, apalike_object):
        assert apalike_object.add_title().title == 'cff-converter-python'

    def test_url(self, apalike_object):
        assert apalike_object.add_url().url == 'URL: https://github.com/citation-file-format/cff-converter-python'

    def test_version(self, apalike_object):
        assert apalike_object.add_version().version == '(version 1.0.0).'

    def test_year(self, apalike_object):
        assert apalike_object.add_year().year == '(2018).'
