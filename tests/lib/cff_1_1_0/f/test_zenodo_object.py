import os
from functools import lru_cache
import pytest
from cffconvert import Citation
from cffconvert.lib.cff_1_1_x.zenodo import ZenodoObject
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
        assert zenodo_object().add_creators().creators == [
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Spaaks, Jurriaan H."
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Klaver, Tom"
            }
        ]

    def test_keywords(self):
        assert zenodo_object().add_keywords().keywords == ["citation", "bibliography", "cff", "CITATION.cff"]

    def test_license(self):
        assert zenodo_object().add_license().license == {"id": "Apache-2.0"}

    def test_publication_date(self):
        assert zenodo_object().add_publication_date().publication_date == "2018-01-16"

    def test_related_identifiers(self):
        assert zenodo_object().add_related_identifiers().related_identifiers == [{
            "identifier": "10.5281/zenodo.1162057",
            "relation": "isSupplementedBy",
            "scheme": "doi"
        }, {
            "identifier": "10.0000/FIXME",
            "relation": "isSupplementedBy",
            "scheme": "doi"
        }, {
            "identifier": "https://github.com/citation-file-format/cffconvert",
            "relation": "isSupplementedBy",
            "scheme": "url"
        }]

    def test_title(self):
        assert zenodo_object().add_title().title == "cffconvert"

    def test_upload_type(self):
        assert zenodo_object().add_upload_type().upload_type == "software"

    def test_version(self):
        assert zenodo_object().add_version().version == "1.0.0"
