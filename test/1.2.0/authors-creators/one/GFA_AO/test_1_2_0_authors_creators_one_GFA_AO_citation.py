import os
import pytest
from cffconvert.citation import Citation


@pytest.fixture(scope="module")
def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffversion(citation):
    assert citation.cffversion == "1.2.0"


def test_validate(citation):
    citation.validate()
