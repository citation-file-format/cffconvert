import json
import os
from ruamel.yaml import YAML
from cffconvert.version import __version__ as expected_version


def test_version_number_cff():
    # CITATION.cff content should have the same semver as setup.cfg / version.py
    fixture = os.path.join("CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as fid:
        cff_contents = fid.read()
    actual_version = YAML(typ='safe').load(cff_contents)["version"]
    assert expected_version == actual_version


def test_zenodo_has_no_version_number():
    # .zenodo.json content should not have any semver information, Zenodo retrieves this automatically from the
    # Zenodo-GitHub integration
    fixture = os.path.join(".zenodo.json")
    with open(fixture, "rt", encoding="utf-8") as fid:
        zenodojson_contents = fid.read()
    assert "version" not in json.loads(zenodojson_contents).keys()


def test_zenodo_has_no_doi():
    # .zenodo.json content should not have any doi information since you cannot tell Zenodo what the doi should be
    fixture = os.path.join(".zenodo.json")
    with open(fixture, "rt", encoding="utf-8") as fid:
        zenodojson_contents = fid.read()
    assert "doi" not in json.loads(zenodojson_contents).keys()


def test_zenodo_has_no_date_published():
    # .zenodo.json content should not have any date information, the Zenodo-GitHub integration assigns
    # the date as today's date
    fixture = os.path.join(".zenodo.json")
    with open(fixture, "rt", encoding="utf-8") as fid:
        zenodojson_contents = fid.read()
    assert "publication_date" not in json.loads(zenodojson_contents).keys()
