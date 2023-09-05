import os
from functools import lru_cache
import pytest
from cffconvert import Citation
from cffconvert.lib.cff_1_3_x.zenodo import ZenodoObject
from tests.lib.contracts.zenodo import Contract


@lru_cache
def zenodo_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ZenodoObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.zenodo
class TestZenodoObject(Contract):

    def test_as_string(self):
        actual_zenodo = zenodo_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_zenodo = f.read()
        assert actual_zenodo == expected_zenodo

    def test_check_cffobj(self):
        zenodo_object().check_cffobj()
        # doesn't need an assert

    def test_contributors(self):
        assert zenodo_object().add_contributors().contributors is None

    def test_creators(self):
        assert zenodo_object().add_creators().creators == [{
            "name": "Test author"
        }]

    def test_keywords(self):
        assert zenodo_object().add_keywords().keywords is None

    def test_license(self):
        assert zenodo_object().add_license().license is None

    def test_publication_date(self):
        assert zenodo_object().add_publication_date().publication_date is None

    def test_related_identifiers(self):
        assert zenodo_object().add_related_identifiers().related_identifiers == [{
            "identifier": "https://github.com/the-url-from-identifiers",
            "relation": "isSupplementedBy",
            "scheme": "url"
        }, {
            "identifier": "https://github.com/the-url-from-repository-artifact",
            "relation": "isSupplementedBy",
            "scheme": "url"
        }, {
            "identifier": "https://github.com/the-url-from-repository-code",
            "relation": "isSupplementedBy",
            "scheme": "url"
        }, {
            "identifier": "https://github.com/the-url-from-url",
            "relation": "isSupplementedBy",
            "scheme": "url"
        }]

    def test_title(self):
        assert zenodo_object().add_title().title == "Test title"

    def test_upload_type(self):
        assert zenodo_object().add_upload_type().upload_type == "software"

    def test_version(self):
        assert zenodo_object().add_version().version is None
