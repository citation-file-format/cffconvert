import os
import pytest
from test.contracts.endnote_object import Contract
from cffconvert.behavior_1_2_x.endnote.endnote import EndnoteObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class TestEndnoteObject(Contract):

    def test_check_cffobj(self, endnote_object):
        endnote_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, endnote_object):
        assert endnote_object.add_author().author == '%A von der Spaaks Jr., Jurriaan H.\n'

    def test_doi(self, endnote_object):
        assert endnote_object.add_doi().doi is None

    def test_keyword(self, endnote_object):
        assert endnote_object.add_keyword().keyword is None

    def test_name(self, endnote_object):
        assert endnote_object.add_name().name == '%T the title\n'

    def test_print(self, endnote_object):
        actual_endnote = endnote_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_url(self, endnote_object):
        assert endnote_object.add_url().url is None

    def test_year(self, endnote_object):
        assert endnote_object.add_year().year is None
