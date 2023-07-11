import os
import pytest
from test.contracts.zenodo_object import Contract
from cffconvert.behavior_1_0_x.zenodo_object import ZenodoObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def zenodo_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ZenodoObject(citation.cffobj, initialize_empty=True)


class TestZenodoObject(Contract):

    def test_as_string(self, zenodo_object):
        actual_zenodo = zenodo_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_zenodo = f.read()
        assert actual_zenodo == expected_zenodo

    def test_check_cffobj(self, zenodo_object):
        zenodo_object.check_cffobj()
        # doesn't need an assert

    def test_creators(self, zenodo_object):
        assert zenodo_object.add_creators().creators == [
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Spaaks, Jurriaan H."
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Klaver, Tom"
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Verhoeven, Stefan"
            },
            {
                "affiliation": "Humboldt-Universität zu Berlin",
                "name": "Druskat, Stephan",
                "orcid": "0000-0003-4925-7248"
            }
        ]

    def test_keywords(self, zenodo_object):
        assert zenodo_object.add_keywords().keywords == ['citation', 'bibliography', 'cff', 'CITATION.cff']

    def test_license(self, zenodo_object):
        assert zenodo_object.add_license().license == dict(id='Apache-2.0')

    def test_publication_date(self, zenodo_object):
        assert zenodo_object.add_publication_date().publication_date == '2018-07-25'

    def test_title(self, zenodo_object):
        assert zenodo_object.add_title().title == 'cffconvert'

    def test_upload_type(self, zenodo_object):
        assert zenodo_object.add_upload_type().upload_type == 'software'

    def test_version(self, zenodo_object):
        assert zenodo_object.add_version().version == '1.0.1'
