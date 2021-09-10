import os
import pytest
from test.contracts.bibtex_object import Contract
from cffconvert.behavior_1_2_x.bibtex.bibtex import BibtexObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def bibtex_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return BibtexObject(citation.cffobj, initialize_empty=True)


class TestBibtexObject(Contract):

    def test_author(self, bibtex_object):
        bibtex_object.add_author()
        assert bibtex_object.author == 'author = {van der Vaart III, Rafael and dos Santos Aveiro, Cristiano Ronaldo}'

    def test_check_cffobj(self, bibtex_object):
        bibtex_object.check_cffobj()
        # doesn't need an assert

    def test_doi(self, bibtex_object):
        bibtex_object.add_doi()
        assert bibtex_object.doi is None

    def test_month(self, bibtex_object):
        bibtex_object.add_month()
        assert bibtex_object.month is None

    def test_print(self, bibtex_object):
        actual_bibtex = bibtex_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_bibtex = f.read()
        assert actual_bibtex == expected_bibtex

    def test_title(self, bibtex_object):
        bibtex_object.add_title()
        assert bibtex_object.title == 'title = {the title}'

    def test_url(self, bibtex_object):
        bibtex_object.add_url()
        assert bibtex_object.url is None

    def test_year(self, bibtex_object):
        bibtex_object.add_year()
        assert bibtex_object.year is None
