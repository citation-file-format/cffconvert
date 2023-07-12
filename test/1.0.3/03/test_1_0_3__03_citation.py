import datetime
import os
import pytest
import pykwalify
from cffconvert.citation import Citation


def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffobj():
    assert type(citation().cffobj["date-released"]) is datetime.date
    assert citation().cffobj["date-released"] == datetime.date(year=2017, month=10, day=7)


def test_cffversion():
    assert citation().cffversion == "1.0.3"


def test_validate():
    with pytest.raises(pykwalify.errors.SchemaError) as e:
        citation().validate()
    msg = str(e.value)
    # ORCIDs ending in X were not supported in 1.0.3
    assert "Value 'https://orcid.org/0000-0002-0989-929X' does not match pattern" in msg
