import os
import pytest


def get_formats():
    return [
        pytest.param("apalike", "apalike.txt", id="apalike", marks=pytest.mark.apalike),
        pytest.param("bibtex", "bibtex.bib", id="bibtex", marks=pytest.mark.bibtex),
        pytest.param("cff", "CITATION.cff", id="cff"),
        pytest.param("codemeta", "codemeta.json", id="codemeta", marks=pytest.mark.codemeta),
        pytest.param("endnote", "endnote.enw", id="endnote", marks=pytest.mark.endnote),
        pytest.param("ris", "ris.txt", id="ris", marks=pytest.mark.ris),
        pytest.param("schema.org", "schemaorg.json", id="schema.org", marks=pytest.mark.schemaorg),
        pytest.param("zenodo", ".zenodo.json", id="zenodo", marks=pytest.mark.zenodo)
    ]


def read_sibling_file(myfile, filename):
    mydir = os.path.dirname(myfile)
    fixture = os.path.join(mydir, filename)
    with open(fixture, "rt", encoding="utf-8") as fid:
        return fid.read()
