import os
import pytest
from test.contracts.ris_object import Contract
from cffconvert.behavior_1_0_x.ris.ris import RisObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def ris_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return RisObject(citation.cffobj, initialize_empty=True)


class TestRisObject(Contract):

    def test_abstract(self, ris_object):
        assert ris_object.add_abstract().abstract is None

    def test_as_string(self, ris_object):
        actual_ris = ris_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "ris.txt")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_ris = f.read()
        assert actual_ris == expected_ris

    def test_author(self, ris_object):
        assert ris_object.add_author().author == 'AU  - Spaaks, Jurriaan H.\nAU  - Klaver, Tom\n' + \
                                    'AU  - Verhoeven, Stefan\nAU  - Druskat, Stephan\n'

    def test_check_cffobj(self, ris_object):
        ris_object.check_cffobj()
        # doesn't need an assert

    def test_date(self, ris_object):
        assert ris_object.add_date().date == 'DA  - 2018-07-25\n'

    def test_doi(self, ris_object):
        assert ris_object.add_doi().doi == 'DO  - 10.5281/zenodo.1162057\n'

    def test_keywords(self, ris_object):
        assert ris_object.add_keywords().keywords == 'KW  - citation\nKW  - bibliography\nKW  - cff\nKW  - CITATION.cff\n'

    def test_title(self, ris_object):
        assert ris_object.add_title().title == 'TI  - cffconvert\n'

    def test_url(self, ris_object):
        assert ris_object.add_url().url == 'UR  - https://github.com/citation-file-format/cff-converter-python\n'

    def test_year(self, ris_object):
        assert ris_object.add_year().year == 'PY  - 2018\n'
