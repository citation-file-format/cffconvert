import os
import pytest
from test.contracts.codemeta_object import Contract
from cffconvert.behavior_1_0_x.codemeta.codemeta import CodemetaObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def codemeta_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return CodemetaObject(citation.cffobj, initialize_empty=True)


class TestCodemetaObject(Contract):

    def test_as_string(self, codemeta_object):
        actual_codemeta = codemeta_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_codemeta = f.read()
        assert actual_codemeta == expected_codemeta

    def test_author(self, codemeta_object):
        assert codemeta_object.add_author().author == [{
            "@type": "Person",
            "givenName": "Jisk",
            "familyName": "Attema",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            }
        }, {
            "@id": "https://orcid.org/0000-0002-0989-929X",
            "@type": "Person",
            "givenName": "Faruk",
            "familyName": "Diblen",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            }
        }]

    def test_check_cffobj(self, codemeta_object):
        codemeta_object.check_cffobj()
        # doesn't need an assert

    def test_code_repository(self, codemeta_object):
        assert codemeta_object.add_code_repository().code_repository == 'https://github.com/NLeSC/spot'

    def test_date_published(self, codemeta_object):
        assert codemeta_object.add_date_published().date_published == '2017-10-07'

    def test_description(self, codemeta_object):
        assert codemeta_object.add_description().description is None

    def test_identifier(self, codemeta_object):
        assert codemeta_object.add_identifier().identifier == 'https://doi.org/10.5281/zenodo.1003346'

    def test_keywords(self, codemeta_object):
        assert codemeta_object.add_keywords().keywords == [
            'visualization',
            'big data',
            'visual data analytics',
            'multi-dimensional data'
        ]

    def test_license(self, codemeta_object):
        assert codemeta_object.add_license().license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, codemeta_object):
        assert codemeta_object.add_name().name == 'spot'

    def test_version(self, codemeta_object):
        assert codemeta_object.add_version().version == '0.1.0'
