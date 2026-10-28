import datetime
from pathlib import Path

from cffconvert.lib.citation import Citation


def citation():
    p = Path(__file__).parent / "CITATION.cff"
    cffstr = p.read_text(encoding="utf-8")
    return Citation(cffstr)


def test_cffobj():
    assert isinstance(citation().cffobj["date-released"], datetime.date)
    assert citation().cffobj["date-released"] == datetime.date(year=2018, month=1, day=16)


def test_cffversion():
    assert citation().cffversion == "1.0.3"


def test_validate():
    citation().validate(verbose=False)
