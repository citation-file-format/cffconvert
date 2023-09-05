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
            "@id": "https://orcid.org/0000-0002-0948-1176",
            "@type": "Person",
            "givenName": "Jisk",
            "familyName": "Attema",
            "affiliation": {
                "@type": "Organization",
                "name": "Netherlands eScience Center"
            }
        }, {
            "@type": "Person",
            "givenName": "Faruk",
            "familyName": "Diblen",
            "affiliation": {
                "@type": "Organization",
                "name": "Netherlands eScience Center"
            }
        }]

    def test_check_cffobj(self):
        codemeta_object().check_cffobj()
        # doesn't need an assert

    def test_code_repository(self):
        assert codemeta_object().add_urls().code_repository == "https://github.com/NLeSC/spot"

    def test_date_published(self):
        assert codemeta_object().add_date_published().date_published == "2017-10-07"

    def test_description(self):
        assert codemeta_object().add_description().description is None

    def test_identifier(self):
        assert codemeta_object().add_identifier().identifier == "https://doi.org/10.5281/zenodo.1003346"

    def test_keywords(self):
        assert codemeta_object().add_keywords().keywords == [
            "visualization",
            "big data",
            "visual data analytics",
            "multi-dimensional data"
        ]

    def test_license(self):
        assert codemeta_object().add_license().license == "https://spdx.org/licenses/Apache-2.0"

    def test_name(self):
        assert codemeta_object().add_name().name == "spot"

    def test_url(self):
        assert codemeta_object().add_urls().url == "https://github.com/NLeSC/spot"

    def test_version(self):
        assert codemeta_object().add_version().version == "0.1.0"
