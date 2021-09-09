import os
import pytest
from test.contracts.ZenodoObject import Contract
from cffconvert.behavior_1_0_x.zenodo.zenodo import ZenodoObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def zenodo_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ZenodoObject(citation.cffobj, initialize_empty=True)


class TestZenodoObject(Contract):

    def test_check_cffobj(self, zenodo_object):
        zenodo_object.check_cffobj()
        # doesn't need an assert

    def test_creators(self, zenodo_object):
        zenodo_object.add_creators()
        expected_creators = [
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Attema, Jisk"
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Diblen, Faruk",
                "orcid": "0000-0002-0989-929X"
            }
        ]
        assert zenodo_object.creators == expected_creators

    def test_keywords(self, zenodo_object):
        zenodo_object.add_keywords()
        assert zenodo_object.keywords == ['visualization', 'big data', 'visual data analytics', 'multi-dimensional data']

    def test_license(self, zenodo_object):
        zenodo_object.add_license()
        assert zenodo_object.license == dict(id='Apache-2.0')

    def test_print(self, zenodo_object):
        actual_zenodo = zenodo_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "r", encoding="utf8") as f:
            expected_zenodo = f.read()
        assert actual_zenodo == expected_zenodo

    def test_publication_date(self, zenodo_object):
        zenodo_object.add_publication_date()
        assert zenodo_object.publication_date == '2017-10-07'

    def test_title(self, zenodo_object):
        zenodo_object.add_title()
        assert zenodo_object.title == 'spot'

    def test_version(self, zenodo_object):
        zenodo_object.add_version()
        assert zenodo_object.version == '0.1.0'
