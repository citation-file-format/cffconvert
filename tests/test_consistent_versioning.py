import json
import os
import re
from ruamel.yaml import YAML


def get_version_from_pyproject_toml():
    fixture = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^version = "(?P<version>\S*)"$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    return actual_version


def test_citation_cff():
    fixture = os.path.join(os.path.dirname(__file__), "..", "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    actual_version = YAML(typ="safe").load(file_contents)["version"]
    assert actual_version == expected_version


def test_zenodo_json():
    fixture = os.path.join(os.path.dirname(__file__), "..", ".zenodo.json")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    actual_version = json.loads(file_contents)["version"]
    assert actual_version == expected_version


def test_dockerfile():
    fixture = os.path.join(os.path.dirname(__file__), "..", "Dockerfile")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^RUN .* cffconvert==(?P<version>\S*)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_alternative_install_options_md():
    fixture = os.path.join(os.path.dirname(__file__), "..", "docs", "alternative-install-options.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^docker build --tag cffconvert:(?P<version>\S*) .$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_1():
    fixture = os.path.join(os.path.dirname(__file__), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^# \(requires (?P<version>\S*) to be downloadable from PyPI\)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_2():
    fixture = os.path.join(os.path.dirname(__file__), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^docker build --tag cffconvert:(?P<version>\S*) .$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_3():
    fixture = os.path.join(os.path.dirname(__file__), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^docker tag cffconvert:(?P<version1>\S*) citationcff/" +
                       r"cffconvert:(?P<version2>\S*)$", re.MULTILINE)
    actual_version_1 = re.search(regex, file_contents)["version1"]
    actual_version_2 = re.search(regex, file_contents)["version2"]
    assert actual_version_1 == expected_version
    assert actual_version_2 == expected_version


def test_readme_dev_md_4():
    fixture = os.path.join(os.path.dirname(__file__), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"^docker push citationcff/cffconvert:(?P<version>\S*)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_authors_keys_readme():
    fixture = os.path.join(os.path.dirname(__file__), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r"blob/(?P<version>\S*)/cffconvert", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


expected_version = get_version_from_pyproject_toml()
