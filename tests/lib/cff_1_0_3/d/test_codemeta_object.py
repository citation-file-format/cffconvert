import os
from functools import lru_cache
import pytest
from cffconvert import Citation
from cffconvert.lib.cff_1_0_x.codemeta import CodemetaObject
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
            "affiliation": {
                "@type": "Organization",
                "name": "Netherlands eScience Center"
            },
            "familyName": "Spaaks",
            "givenName": "Jurriaan H."
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": "Netherlands eScience Center"
            },
            "familyName": "Klaver",
            "givenName": "Tom"
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": "Netherlands eScience Center"
            },
            "familyName": "Verhoeven",
            "givenName": "Stefan"
        }, {
            "@id": "https://orcid.org/0000-0003-4925-7248",
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "name": "Humboldt-Universität zu Berlin"
            },
            "familyName": "Druskat",
            "givenName": "Stephan"
        }]

    def test_check_cffobj(self):
        codemeta_object().check_cffobj()
        # doesn't need an assert

    def test_code_repository(self):
        assert codemeta_object().add_urls().code_repository == "https://github.com/citation-file-format" + \
                                                               "/cffconvert"

    def test_date_published(self):
        assert codemeta_object().add_date_published().date_published == "2018-07-25"

    def test_description(self):
        assert codemeta_object().add_description().description is None

    def test_identifier(self):
        assert codemeta_object().add_identifier().identifier == "https://doi.org/10.5281/zenodo.1162057"

    def test_keywords(self):
        assert codemeta_object().add_keywords().keywords == ["citation", "bibliography", "cff", "CITATION.cff"]

    def test_license(self):
        assert codemeta_object().add_license().license == "https://spdx.org/licenses/Apache-2.0"

    def test_name(self):
        assert codemeta_object().add_name().name == "cffconvert"

    def test_url(self):
        assert codemeta_object().add_urls().url == "https://github.com/citation-file-format/cffconvert"

    def test_version(self):
        assert codemeta_object().add_version().version == "1.0.1"
