import os
from functools import lru_cache
import pytest
from cffconvert import Citation
from cffconvert.lib.cff_1_2_x.bibtex import BibtexObject
from tests.lib.contracts.bibtex import Contract


@lru_cache
def bibtex_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return BibtexObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.bibtex
class TestBibtexObject(Contract):

    def test_author(self):
        assert bibtex_object().add_author().author == "author = {{Test author}}"

    def test_check_cffobj(self):
        bibtex_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert bibtex_object().add_doi().doi is None

    def test_month(self):
        assert bibtex_object().add_month().month is None

    def test_as_string(self):
        actual_bibtex = bibtex_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_bibtex = f.read()
        assert actual_bibtex == expected_bibtex

    def test_title(self):
        assert bibtex_object().add_title().title == "title = {Test title}"

    def test_url(self):
        assert bibtex_object().add_url().url is None

    def test_year(self):
        assert bibtex_object().add_year().year is None
