import os
from cffconvert.lib.citation import Citation


def citation():
    p = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(p, "rt", encoding="utf-8") as fid:
        cffstr = fid.read()
        return Citation(cffstr)


def test_cffversion():
    assert citation().cffversion == "1.3.0"


def test_validate():
    citation().validate(verbose=False)
