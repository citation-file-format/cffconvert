from functools import lru_cache
from pathlib import Path

import pytest

from cffconvert import Citation
from cffconvert.lib.cff_1_3_x.schemaorg import SchemaorgObject
from tests.lib.contracts.schemaorg import Contract


@lru_cache
def schemaorg_object():
    fixture = Path(__file__).parent / "CITATION.cff"
    cffstr = fixture.read_text(encoding="utf-8")
    citation = Citation(cffstr)
    return SchemaorgObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.schemaorg
class TestSchemaorgObject(Contract):

    def test_as_string(self):
        actual_schemaorg = schemaorg_object().add_all().as_string()
        fixture = Path(__file__).parent / "schemaorg.json"
        expected_schemaorg = fixture.read_text(encoding="utf-8")
        assert actual_schemaorg == expected_schemaorg

    def test_author(self):
        assert schemaorg_object().add_author().author == [{
            "@type": "Person",
            "alternateName": "Rafa"
        }]

    def test_check_cffobj(self):
        schemaorg_object().check_cffobj()
        # doesn't need an assert

    def test_code_repository(self):
        assert schemaorg_object().add_urls().code_repository is None

    def test_contributor(self):
        assert schemaorg_object().add_contributor().contributor is None

    def test_date_published(self):
        assert schemaorg_object().add_date_published().date_published is None

    def test_description(self):
        assert schemaorg_object().add_description().description is None

    def test_identifier(self):
        assert schemaorg_object().add_identifier().identifier is None

    def test_keywords(self):
        assert schemaorg_object().add_keywords().keywords is None

    def test_license(self):
        assert schemaorg_object().add_license().license is None

    def test_name(self):
        assert schemaorg_object().add_name().name == "the title"

    def test_upload_type(self):
        assert schemaorg_object().add_type().type == "SoftwareSourceCode"

    def test_url(self):
        assert schemaorg_object().add_urls().url is None

    def test_version(self):
        assert schemaorg_object().add_version().version is None
