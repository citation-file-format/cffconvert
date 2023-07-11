import os
from test.contracts.schemaorg_object import Contract
import pytest
from cffconvert import Citation
from cffconvert.behavior_1_0_x.schemaorg_object import SchemaorgObject


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

    def test_check_cffobj(self, schemaorg_object):
        schemaorg_object.check_cffobj()
        # doesn't need an assert

    def test_code_repository(self, schemaorg_object):
        assert schemaorg_object.add_urls().code_repository == 'https://github.com/NLeSC/spot'

    def test_date_published(self, schemaorg_object):
        assert schemaorg_object.add_date_published().date_published == '2017-10-07'

    def test_description(self, schemaorg_object):
        assert schemaorg_object.add_description().description is None

    def test_identifier(self, schemaorg_object):
        assert schemaorg_object.add_identifier().identifier == 'https://doi.org/10.5281/zenodo.1003346'

    def test_keywords(self, schemaorg_object):
        assert schemaorg_object.add_keywords().keywords == [
            'visualization',
            'big data',
            'visual data analytics',
            'multi-dimensional data'
        ]

    def test_license(self, schemaorg_object):
        assert schemaorg_object.add_license().license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, schemaorg_object):
        assert schemaorg_object.add_name().name == 'spot'

    def test_url(self, schemaorg_object):
        assert schemaorg_object.add_urls().url == 'https://github.com/NLeSC/spot'

    def test_version(self, schemaorg_object):
        assert schemaorg_object.add_version().version == '0.1.0'
