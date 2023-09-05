import os
from functools import lru_cache
import pytest
from cffconvert import Citation
from cffconvert.lib.cff_1_2_x.codemeta import CodemetaObject
from tests.lib.contracts.codemeta import Contract


@lru_cache
def codemeta_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return CodemetaObject(citation.cffobj, initialize_empty=True)


@pytest.mark.lib
@pytest.mark.codemeta
class TestCodemetaObject(Contract):

    def test_as_string(self):
        actual_codemeta = codemeta_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_codemeta = f.read()
        assert actual_codemeta == expected_codemeta

    def test_author(self):
        assert codemeta_object().add_author().author == [{
            "@type": "Person",
            "familyName": "van der Vaart III",
            "givenName": "Rafael"
        }, {
            "@type": "Person",
            "familyName": "dos Santos Aveiro",
            "givenName": "Cristiano Ronaldo"
        }]

    def test_check_cffobj(self):
        codemeta_object().check_cffobj()
        # doesn't need an assert

    def test_code_repository(self):
        assert codemeta_object().add_urls().code_repository is None

    def test_contributor(self):
        assert codemeta_object().add_contributor().contributor is None

    def test_date_published(self):
        assert codemeta_object().add_date_published().date_published is None

    def test_description(self):
        assert codemeta_object().add_description().description is None

    def test_identifier(self):
        assert codemeta_object().add_identifier().identifier is None

    def test_keywords(self):
        assert codemeta_object().add_keywords().keywords is None

    def test_license(self):
        assert codemeta_object().add_license().license is None

    def test_name(self):
        assert codemeta_object().add_name().name == "the title"

    def test_upload_type(self):
        assert codemeta_object().add_type().type == "SoftwareSourceCode"

    def test_url(self):
        assert codemeta_object().add_urls().url is None

    def test_version(self):
        assert codemeta_object().add_version().version is None
