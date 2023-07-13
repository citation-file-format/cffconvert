import os
from tests.contracts.endnote_object import Contract
from cffconvert import Citation
from cffconvert.cff_1_0_x.endnote import EndnoteObject


def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class TestEndnoteObject(Contract):

    def test_as_string(self):
        actual_endnote = endnote_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_author(self):
        assert endnote_object().add_author().author == '%A Attema, Jisk\n%A Diblen, Faruk\n'

    def test_check_cffobj(self):
        endnote_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert endnote_object().add_doi().doi == '%R 10.5281/zenodo.1003346\n'

    def test_keyword(self):
        assert endnote_object().add_keyword().keyword == '%K visualization\n%K big data\n' + \
                                                         '%K visual data analytics\n%K multi-dimensional data\n'

    def test_name(self):
        assert endnote_object().add_name().name == '%T spot\n'

    def test_url(self):
        assert endnote_object().add_url().url == '%U https://github.com/NLeSC/spot\n'

    def test_year(self):
        assert endnote_object().add_year().year == '%D 2017\n'
