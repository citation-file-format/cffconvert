from functools import lru_cache
from pathlib import Path

import pytest

from cffconvert import Citation
from cffconvert.lib.cff_1_0_x.apalike import ApalikeObject
from tests.lib.contracts.apalike import Contract


@lru_cache
def apalike_object():
    fixture = Path(__file__).parent / "CITATION.cff"
    cffstr = fixture.read_text(encoding="utf-8")
    citation = Citation(cffstr)
    return ApalikeObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.apalike
class TestApalikeObject(Contract):

    def test_as_string(self):
        actual_apalike = apalike_object().add_all().as_string()
        fixture = Path(__file__).parent / "apalike.txt"
        expected_apalike = fixture.read_text(encoding="utf-8")
        assert actual_apalike == expected_apalike

    def test_author(self):
        assert apalike_object().add_author().author == "Attema J. and Diblen F."

    def test_check_cffobj(self):
        apalike_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert apalike_object().add_doi().doi == "DOI: 10.5281/zenodo.1003346"

    def test_title(self):
        assert apalike_object().add_title().title == "spot"

    def test_url(self):
        assert apalike_object().add_url().url == "URL: https://github.com/NLeSC/spot"

    def test_version(self):
        assert apalike_object().add_version().version == "(version 0.1.0)."

    def test_year(self):
        assert apalike_object().add_year().year == "(2017)."
