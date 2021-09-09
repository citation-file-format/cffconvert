import os
import pytest
from test.contracts.RisObject import Contract
from cffconvert.behavior_1_2_x.ris.ris import RisObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def ris_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return RisObject(citation.cffobj, initialize_empty=True)


class TestRisObject(Contract):

    def test_abstract(self, ris_object):
        ris_object.add_abstract()
        assert ris_object.abstract is None

    def test_author(self, ris_object):
        ris_object.add_author()
        assert ris_object.author == 'AU  - von der Spaaks Jr., Jurriaan H.\n'

    def test_check_cffobj(self, ris_object):
        ris_object.check_cffobj()
        # doesn't need an assert

    def test_date(self, ris_object):
        ris_object.add_date()
        assert ris_object.date is None

    def test_doi(self, ris_object):
        ris_object.add_doi()
        assert ris_object.doi is None

    def test_keywords(self, ris_object):
        ris_object.add_keywords()
        assert ris_object.keywords is None

    def test_print(self, ris_object):
        actual_ris = ris_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        assert actual_ris == expected_ris

    def test_title(self, ris_object):
        ris_object.add_title()
        assert ris_object.title == 'TI  - the title\n'

    def test_url(self, ris_object):
        ris_object.add_url()
        assert ris_object.url is None

    def test_year(self, ris_object):
        ris_object.add_year()
        assert ris_object.year is None
