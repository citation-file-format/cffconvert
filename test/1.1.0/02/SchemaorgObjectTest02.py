import os
import pytest
from test.contracts.SchemaorgObject import Contract
from cffconvert.schemaorg import SchemaorgObject
from cffconvert import Citation


@pytest.fixture
def schemorg_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return SchemaorgObject(citation.cffobj, initialize_empty=True)


class SchemaorgObjectTest(Contract):

    def test_check_cff_object(self, schemorg_object):
        schemorg_object.check_cff_object()
        # doesn't need an assert

    def test_author(self, schemorg_object):
        schemorg_object.add_author()
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
        }]
        assert schemorg_object.author == expected_author

    def test_code_repository(self, schemorg_object):
        schemorg_object.add_code_repository()
        assert schemorg_object.code_repository == 'https://github.com/citation-file-format/cff-converter-python'

    def test_date_published(self, schemorg_object):
        schemorg_object.add_date_published()
        assert schemorg_object.date_published == '2018-01-16'

    def test_description(self, schemorg_object):
        schemorg_object.add_description()
        assert schemorg_object.description is None

    def test_identifier(self, schemorg_object):
        schemorg_object.add_identifier()
        assert schemorg_object.identifier == 'https://doi.org/10.5281/zenodo.1162057'

    def test_keywords(self, schemorg_object):
        schemorg_object.add_keywords()
        expected_keywords = ['citation', 'bibliography', 'cff', 'CITATION.cff']
        assert schemorg_object.keywords == expected_keywords

    def test_license(self, schemorg_object):
        schemorg_object.add_license()
        assert schemorg_object.license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, schemorg_object):
        schemorg_object.add_name()
        assert schemorg_object.name == 'cff-converter-python'

    def test_version(self, schemorg_object):
        schemorg_object.add_version()
        assert schemorg_object.version == '1.0.0'

    def test_print(self, schemorg_object):
        actual_schemaorg = schemorg_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "schemaorg.json")
        with open(fixture, "r", encoding="utf8") as f:
            expected_schemaorg = f.read()
        assert actual_schemaorg == expected_schemaorg
