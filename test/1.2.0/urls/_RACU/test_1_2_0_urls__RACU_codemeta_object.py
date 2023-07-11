import os
from test.contracts.codemeta_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_2_x.codemeta_object import CodemetaObject


@pytest.fixture(scope="module")
def codemeta_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return CodemetaObject(citation.cffobj, initialize_empty=True)


class TestCodemetaObject(Contract):

    def test_check_cffobj(self, codemeta_object):
        codemeta_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, codemeta_object):
        assert codemeta_object.add_author().author == [{
            "@type": "Person",
            "name": "Test author"
        }]

    def test_code_repository(self, codemeta_object):
        assert codemeta_object.add_urls().code_repository == "https://github.com/the-url-from-repository-code"

    def test_date_published(self, codemeta_object):
        assert codemeta_object.add_date_published().date_published is None

    def test_description(self, codemeta_object):
        assert codemeta_object.add_description().description is None

    def test_identifier(self, codemeta_object):
        assert codemeta_object.add_identifier().identifier is None

    def test_keywords(self, codemeta_object):
        assert codemeta_object.add_keywords().keywords is None

    def test_license(self, codemeta_object):
        assert codemeta_object.add_license().license is None

    def test_name(self, codemeta_object):
        assert codemeta_object.add_name().name == 'Test title'

    def test_upload_type(self, codemeta_object):
        assert codemeta_object.add_type().type == "SoftwareSourceCode"

    def test_url(self, codemeta_object):
        assert codemeta_object.add_urls().url == "https://github.com/the-url-from-url"

    def test_version(self, codemeta_object):
        assert codemeta_object.add_version().version is None

    def test_as_string(self, codemeta_object):
        actual_schemaorg = codemeta_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg
