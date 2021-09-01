import os
import pytest
from test.contracts.EndnoteObject import Contract
from cffconvert import EndnoteObject
from cffconvert import Citation


@pytest.fixture
def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class EndnoteObjectTest(Contract):

    def test_check_cff_object(self, endnote_object):
        endnote_object.check_cff_object()
        # doesn't need an assert

    def test_author(self, endnote_object):
        endnote_object.add_author()
        assert endnote_object.author == '%A Attema, Jisk\n%A Diblen, Faruk\n'

    def test_doi(self, endnote_object):
        endnote_object.add_doi()
        assert endnote_object.doi == '%R 10.5281/zenodo.1003346\n'

    def test_keyword(self, endnote_object):
        endnote_object.add_keyword()
        assert endnote_object.keyword == '%K visualization\n%K big data\n%K visual data analytics\n%K multi-dimensional data\n'

    def test_name(self, endnote_object):
        endnote_object.add_name()
        assert endnote_object.name == '%T spot\n'

    def test_print(self, endnote_object):
        actual_endnote = endnote_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "r", encoding="utf8") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_url(self, endnote_object):
        endnote_object.add_url()
        assert endnote_object.url == '%U https://github.com/NLeSC/spot\n'

    def test_year(self, endnote_object):
        endnote_object.add_year()
        assert endnote_object.year == '%D 2017\n'
