import datetime
import os
import pytest
from cffconvert.citation import Citation


@pytest.fixture(scope="module")
def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffobj(citation):
    assert type(citation.cffobj["date-released"]) is datetime.date
    assert citation.cffobj["date-released"] == datetime.date(year=1999, month=12, day=31)


def test_cffversion(citation):
    assert citation.cffversion == "1.0.3"


def test_validate(citation):
    citation.validate()
