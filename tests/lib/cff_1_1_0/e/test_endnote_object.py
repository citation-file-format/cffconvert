from functools import lru_cache
from pathlib import Path

import pytest

from cffconvert import Citation
from cffconvert.lib.cff_1_1_x.endnote import EndnoteObject
from tests.lib.contracts.endnote import Contract


@lru_cache
def endnote_object():
    fixture = Path(__file__).parent / "CITATION.cff"
    cffstr = fixture.read_text(encoding="utf-8")
    citation = Citation(cffstr)
    return EndnoteObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.endnote
class TestEndnoteObject(Contract):

    def test_as_string(self):
        actual_endnote = endnote_object().add_all().as_string()
        fixture = Path(__file__).parent / "endnote.enw"
        expected_endnote = fixture.read_text(encoding="utf-8")
        assert actual_endnote == expected_endnote

    def test_author(self):
        assert endnote_object().add_author().author == "%A Spaaks, Jurriaan H.\n%A Klaver, Tom\n%A mysteryauthor\n"

    def test_check_cffobj(self):
        endnote_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert endnote_object().add_doi().doi == "%R 10.5281/zenodo.1162057\n"

    def test_keyword(self):
        assert endnote_object().add_keyword().keyword == "%K citation\n%K bibliography\n%K cff\n%K CITATION.cff\n"

    def test_name(self):
        assert endnote_object().add_name().name == "%T cffconvert\n"

    def test_url(self):
        assert endnote_object().add_url().url == "%U https://github.com/citation-file-format/cffconvert\n"

    def test_year(self):
        assert endnote_object().add_year().year == "%D 2018\n"
