from functools import lru_cache
from pathlib import Path

import pytest

from cffconvert import Citation
from cffconvert.lib.cff_1_0_x.ris import RisObject
from tests.lib.contracts.ris import Contract


@lru_cache
def ris_object():
    fixture = Path(__file__).parent / "CITATION.cff"
    cffstr = fixture.read_text(encoding="utf-8")
    citation = Citation(cffstr)
    return RisObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.ris
class TestRisObject(Contract):

    def test_abstract(self):
        assert ris_object().add_abstract().abstract is None

    def test_as_string(self):
        actual_ris = ris_object().add_all().as_string()
        fixture = Path(__file__).parent / "ris.txt"
        expected_ris = fixture.read_text(encoding="utf-8")
        assert actual_ris == expected_ris

    def test_author(self):
        assert ris_object().add_author().author == "AU  - Attema, Jisk\nAU  - Diblen, Faruk\n"

    def test_check_cffobj(self):
        ris_object().check_cffobj()
        # doesn't need an assert

    def test_date(self):
        assert ris_object().add_date().date == "DA  - 2017-10-07\n"

    def test_doi(self):
        assert ris_object().add_doi().doi == "DO  - 10.5281/zenodo.1003346\n"

    def test_keywords(self):
        assert ris_object().add_keywords().keywords == "KW  - visualization\nKW  - big data\n" + \
                                                       "KW  - visual data analytics\nKW  - multi-dimensional data\n"

    def test_title(self):
        assert ris_object().add_title().title == "TI  - spot\n"

    def test_url(self):
        assert ris_object().add_url().url == "UR  - https://github.com/NLeSC/spot\n"

    def test_year(self):
        assert ris_object().add_year().year == "PY  - 2017\n"
