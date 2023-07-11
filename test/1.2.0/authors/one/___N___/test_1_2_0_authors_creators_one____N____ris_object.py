import os
from test.contracts.ris_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_2_x.ris_object import RisObject


@pytest.fixture(scope="module")
def ris_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return RisObject(citation.cffobj, initialize_empty=True)


class TestRisObject(Contract):

    def test_abstract(self, ris_object):
        assert ris_object.add_abstract().abstract is None

    def test_as_string(self, ris_object):
        actual_ris = ris_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "ris.txt")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_ris = f.read()
        assert actual_ris == expected_ris

    def test_author(self, ris_object):
        assert ris_object.add_author().author == 'AU  - The soccer team members\n'

    def test_check_cffobj(self, ris_object):
        ris_object.check_cffobj()
        # doesn't need an assert

    def test_date(self, ris_object):
        assert ris_object.add_date().date is None

    def test_doi(self, ris_object):
        assert ris_object.add_doi().doi is None

    def test_keywords(self, ris_object):
        assert ris_object.add_keywords().keywords is None

    def test_title(self, ris_object):
        assert ris_object.add_title().title == 'TI  - the title\n'

    def test_url(self, ris_object):
        assert ris_object.add_url().url is None

    def test_year(self, ris_object):
        assert ris_object.add_year().year is None
