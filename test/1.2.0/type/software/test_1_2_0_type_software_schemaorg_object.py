import os
from test.contracts.schemaorg_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_2_x.schemaorg_object import SchemaorgObject


@pytest.fixture(scope="module")
def schemaorg_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return SchemaorgObject(citation.cffobj, initialize_empty=True)


class TestSchemaorgObject(Contract):

    def test_as_string(self, schemaorg_object):
        actual_schemaorg = schemaorg_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg

    def test_author(self, schemaorg_object):
        assert schemaorg_object.add_author().author == [{
            "@type": "Person",
            "name": "The name"
        }]

    def test_check_cffobj(self, schemaorg_object):
        schemaorg_object.check_cffobj()
        # doesn't need an assert

    def test_code_repository(self, schemaorg_object):
        assert schemaorg_object.add_urls().code_repository is None

    def test_date_published(self, schemaorg_object):
        assert schemaorg_object.add_date_published().date_published is None

    def test_description(self, schemaorg_object):
        assert schemaorg_object.add_description().description is None

    def test_identifier(self, schemaorg_object):
        assert schemaorg_object.add_identifier().identifier is None

    def test_keywords(self, schemaorg_object):
        assert schemaorg_object.add_keywords().keywords is None

    def test_license(self, schemaorg_object):
        assert schemaorg_object.add_license().license is None

    def test_name(self, schemaorg_object):
        assert schemaorg_object.add_name().name == "The title"

    def test_url(self, schemaorg_object):
        assert schemaorg_object.add_urls().url is None

    def test_upload_type(self, schemaorg_object):
        assert schemaorg_object.add_type().type == "SoftwareSourceCode"

    def test_version(self, schemaorg_object):
        assert schemaorg_object.add_version().version is None
