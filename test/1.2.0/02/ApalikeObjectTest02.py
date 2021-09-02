import os
import pytest
from test.contracts.ApalikeObject import Contract
from cffconvert.apalike import ApalikeObject
from cffconvert import Citation


@pytest.fixture
def apalike_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ApalikeObject(citation.cffobj, initialize_empty=True)


class ApalikeObjectTest(Contract):

    def test_author(self, apalike_object):
        apalike_object.add_author()
        assert apalike_object.author == 'Spaaks J.H., Klaver T.'

    def test_check_cff_object(self, apalike_object):
        apalike_object.check_cff_object()
        # doesn't need an assert

    def test_year(self, apalike_object):
        apalike_object.add_year()
        assert apalike_object.year == ' (2018). '

    def test_title(self, apalike_object):
        apalike_object.add_title()
        assert apalike_object.title == 'cff-converter-python'

    def test_version(self, apalike_object):
        apalike_object.add_version()
        assert apalike_object.version == ' (version 1.0.0). '

    def test_doi(self, apalike_object):
        apalike_object.add_doi()
        assert apalike_object.doi == 'doi: 10.5281/zenodo.1162057. '

    def test_url(self, apalike_object):
        apalike_object.add_url()
        assert apalike_object.url == 'URL: https://github.com/citation-file-format/cff-converter-python\n'
