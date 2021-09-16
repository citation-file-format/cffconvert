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

    def test_check_cffobj(self, codemeta_object):
        codemeta_object.check_cffobj()
        # doesn't need an assert

    def test_code_repository(self, codemeta_object):
        assert codemeta_object.add_urls().code_repository == 'https://github.com/citation-file-format' + \
                                                             '/cff-converter-python'

    def test_date_published(self, codemeta_object):
        assert codemeta_object.add_date_published().date_published == '2018-01-16'

    def test_description(self, codemeta_object):
        assert codemeta_object.add_description().description is None

    def test_identifier(self, codemeta_object):
        assert codemeta_object.add_identifier().identifier == 'https://doi.org/10.5281/zenodo.1162057'

    def test_keywords(self, codemeta_object):
        assert codemeta_object.add_keywords().keywords == ['citation', 'bibliography', 'cff', 'CITATION.cff']

    def test_license(self, codemeta_object):
        assert codemeta_object.add_license().license == 'https://spdx.org/licenses/Apache-2.0'

    def test_name(self, codemeta_object):
        assert codemeta_object.add_name().name == 'cff-converter-python'

    def test_url(self, codemeta_object):
        assert codemeta_object.add_urls().url == 'https://github.com/citation-file-format/cff-converter-python'

    def test_version(self, codemeta_object):
        assert codemeta_object.add_version().version == '1.0.0'
