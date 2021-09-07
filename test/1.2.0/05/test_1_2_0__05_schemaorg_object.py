import os
import pytest
from test.contracts.SchemaorgObject import Contract
from cffconvert.behavior_1_2_x.schemaorg import SchemaorgObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def schemaorg_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return SchemaorgObject(citation.cffobj, initialize_empty=True)


class SchemaorgObjectTest(Contract):

    def test_check_cffobj(self, schemaorg_object):
        schemaorg_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, schemaorg_object):
        schemaorg_object.add_author()
        expected_author = [{
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Spaaks",
            "givenName": "Jurriaan H."
        }, {
            "@type": "Person",
            "affiliation": {
                "@type": "Organization",
                "legalName": "Netherlands eScience Center"
            },
            "familyName": "Klaver",
            "givenName": "Tom"
        }, {
            "@type": "Person",
            "name": "mysteryauthor"
        }]
        assert schemaorg_object.author == expected_author

    def test_code_repository(self, schemaorg_object):
        schemaorg_object.add_code_repository()
        assert schemaorg_object.code_repository == 'https://github.com/citation-file-format/cff-converter-python'

    def test_date_published(self, schemaorg_object):
        schemaorg_object.add_date_published()
        assert schemaorg_object.date_published == '2018-01-16'

    def test_description(self, schemaorg_object):
        schemaorg_object.add_description()
        assert schemaorg_object.description is None

    def test_identifier(self, schemaorg_object):
        schemaorg_object.add_identifier()
        assert schemaorg_object.identifier == 'https://doi.org/10.5281/zenodo.1162057'

    def test_keywords(self, schemaorg_object):
        schemaorg_object.add_keywords()
        expected_keywords = ['citation', 'bibliography', 'cff', 'CITATION.cff']
        assert schemaorg_object.keywords == expected_keywords

    def test_license(self, schemaorg_object):
        schemaorg_object.add_license()
        assert schemaorg_object.license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, schemaorg_object):
        schemaorg_object.add_name()
        assert schemaorg_object.name == 'cff-converter-python'

    def test_version(self, schemaorg_object):
        schemaorg_object.add_version()
        assert schemaorg_object.version == '1.0.0'

    def test_print(self, schemaorg_object):
        actual_schemaorg = schemaorg_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg
