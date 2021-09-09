import os
import pytest
from test.contracts.SchemaorgObject import Contract
from cffconvert.behavior_1_0_x.schemaorg.schemaorg import SchemaorgObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def schemaorg_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return SchemaorgObject(citation.cffobj, initialize_empty=True)


class TestSchemaorgObject(Contract):

    def test_check_cffobj(self, schemaorg_object):
        schemaorg_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, schemaorg_object):
        schemaorg_object.add_author()
        expected_author = [{
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
        assert schemaorg_object.author == expected_author

    def test_code_repository(self, schemaorg_object):
        schemaorg_object.add_code_repository()
        assert schemaorg_object.code_repository == 'https://github.com/NLeSC/spot'

    def test_date_published(self, schemaorg_object):
        schemaorg_object.add_date_published()
        assert schemaorg_object.date_published == '2017-10-07'

    def test_description(self, schemaorg_object):
        schemaorg_object.add_description()
        assert schemaorg_object.description is None

    def test_identifier(self, schemaorg_object):
        schemaorg_object.add_identifier()
        assert schemaorg_object.identifier == 'https://doi.org/10.5281/zenodo.1003346'

    def test_keywords(self, schemaorg_object):
        schemaorg_object.add_keywords()
        expected_keywords = ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data']
        assert schemaorg_object.keywords == expected_keywords

    def test_license(self, schemaorg_object):
        schemaorg_object.add_license()
        assert schemaorg_object.license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, schemaorg_object):
        schemaorg_object.add_name()
        assert schemaorg_object.name == 'spot'

    def test_version(self, schemaorg_object):
        schemaorg_object.add_version()
        assert schemaorg_object.version == '0.1.0'

    def test_print(self, schemaorg_object):
        actual_schemaorg = schemaorg_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r", encoding="utf8") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg
