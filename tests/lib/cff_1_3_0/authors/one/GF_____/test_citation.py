from pathlib import Path

from cffconvert.lib.citation import Citation


def citation():
    p = Path(__file__).parent / "CITATION.cff"
    cffstr = p.read_text(encoding="utf-8")
    return Citation(cffstr)


def test_cffversion():
    assert citation().cffversion == "1.3.0"


def test_validate():
    citation().validate(verbose=False)
