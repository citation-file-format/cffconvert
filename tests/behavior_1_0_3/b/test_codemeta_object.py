import os
from tests.contracts.codemeta_object import Contract
from cffconvert import Citation
from cffconvert.behavior_1_0_x.codemeta_object import CodemetaObject


def codemeta_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return CodemetaObject(citation.cffobj, initialize_empty=True)


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
            "givenName": "Gonzalo",
            "familyName": "Fernández de Córdoba Jr.",
        }]

    def test_check_cffobj(self):
        codemeta_object().check_cffobj()
        # doesn't need an assert

    def test_code_repository(self):
        assert codemeta_object().add_urls().code_repository is None

    def test_date_published(self):
        assert codemeta_object().add_date_published().date_published == "1999-12-31"

    def test_description(self):
        assert codemeta_object().add_description().description is None

    def test_identifier(self):
        assert codemeta_object().add_identifier().identifier is None

    def test_keywords(self):
        assert codemeta_object().add_keywords().keywords is None

    def test_license(self):
        assert codemeta_object().add_license().license is None

    def test_name(self):
        assert codemeta_object().add_name().name == 'example title'

    def test_url(self):
        assert codemeta_object().add_urls().url is None

    def test_version(self):
        assert codemeta_object().add_version().version == '1.0.0'