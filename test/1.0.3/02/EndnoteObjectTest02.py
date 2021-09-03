import os
import pytest
from test.contracts.EndnoteObject import Contract
from cffconvert.behavior_1_0_x.endnote import EndnoteObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class EndnoteObjectTest(Contract):

    def test_check_cffobj(self, endnote_object):
        endnote_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, endnote_object):
        endnote_object.add_author()
        assert endnote_object.author == '%A Fernández de Córdoba Jr., Gonzalo\n'

    def test_doi(self, endnote_object):
        endnote_object.add_doi()
        assert endnote_object.doi is None

    def test_keyword(self, endnote_object):
        endnote_object.add_keyword()
        assert endnote_object.keyword is None

    def test_name(self, endnote_object):
        endnote_object.add_name()
        assert endnote_object.name == '%T example title\n'

    def test_print(self, endnote_object):
        actual_endnote = endnote_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "r", encoding="utf8") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_url(self, endnote_object):
        endnote_object.add_url()
        assert endnote_object.url is None

    def test_year(self, endnote_object):
        endnote_object.add_year()
        assert endnote_object.year == "%D 1999\n"
