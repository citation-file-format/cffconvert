import os
from tests.contracts.bibtex_object import Contract
from cffconvert import Citation
from cffconvert.cff_1_1_x.bibtex_object import BibtexObject


def bibtex_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return BibtexObject(citation.cffobj, initialize_empty=True)


class TestBibtexObject(Contract):

    def test_as_string(self):
        actual_bibtex = bibtex_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_bibtex = f.read()
        assert actual_bibtex == expected_bibtex

    def test_author(self):
        assert bibtex_object().add_author().author == 'author = {Spaaks, Jurriaan H. and Klaver, Tom}'

    def test_check_cffobj(self):
        bibtex_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert bibtex_object().add_doi().doi == 'doi = {10.5281/zenodo.1162057}'

    def test_month(self):
        assert bibtex_object().add_month().month == 'month = {1}'

    def test_title(self):
        assert bibtex_object().add_title().title == 'title = {cff-converter-python}'

    def test_url(self):
        assert bibtex_object().add_url().url == 'url = {https://github.com/citation-file-format/cff-converter-python}'

    def test_year(self):
        assert bibtex_object().add_year().year == 'year = {2018}'
