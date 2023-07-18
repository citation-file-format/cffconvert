import os
import pytest
from cffconvert import Citation
from cffconvert.cff_1_3_x.zenodo import ZenodoObject


def get_cffstr():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        return f.read()


def get_relation_types():
    return [
        "cites",
        "compiles",
        "continues",
        "describes",
        "documents",
        "hasPart",
        "isAlternateIdentifier",
        "isCitedBy",
        "isCompiledBy",
        "isContinuedBy",
        "isDerivedFrom",
        "isDescribedBy",
        "isDocumentedBy",
        "isIdenticalTo",
        "isNewVersionOf",
        "isObsoletedBy",
        "isPartOf",
        "isPreviousVersionOf",
        "isPublishedIn",
        "isReferencedBy",
        "isRequiredBy",
        "isReviewedBy",
        "isSourceOf",
        "isSupplementedBy",
        "isSupplementTo",
        "obsoletes",
        "references",
        "requires",
        "reviews"
    ]


@pytest.mark.parametrize("expected", get_relation_types())
def test_with_relation(expected):

    cffstr = get_cffstr().replace("isCompiledBy", expected)
    citation = Citation(cffstr)
    zenodo_object = ZenodoObject(citation.cffobj, initialize_empty=True)
    actual = zenodo_object.add_related_identifiers() \
                          .related_identifiers[0]    \
                          .get("relation")
    assert actual == expected


def test_without_relation():
    cffstr = get_cffstr().replace("relation: isCompiledBy\n    ", "")
    citation = Citation(cffstr)
    zenodo_object = ZenodoObject(citation.cffobj, initialize_empty=True)
    relation = zenodo_object.add_related_identifiers() \
                            .related_identifiers[0]    \
                            .get("relation")
    assert relation is "isSupplementedBy"
