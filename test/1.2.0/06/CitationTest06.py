import os
import pytest
import jsonschema
from cffconvert.citation import Citation


@pytest.fixture
def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffobj(citation):
    assert type(citation.cffobj["date-released"]) is str
    assert citation.cffobj["date-released"] == "2018-01-16"


def test_cffversion(citation):
    assert citation.cffversion == "1.2.0"


def test_validate(citation):
    with pytest.raises(jsonschema.exceptions.ValidationError) as execinfo:
        citation.validate()
    msg = str(execinfo.value)
    assert "None is not of type 'string'" in msg
    assert "alias" in msg

