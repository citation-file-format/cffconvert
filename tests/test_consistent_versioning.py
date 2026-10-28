import json
import re
from pathlib import Path

from ruamel.yaml import YAML


def get_version_from_pyproject_toml():
    fixture = Path(__file__).parent / ".." / "pyproject.toml"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r'^version = "(?P<version>\S*)"$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    return actual_version


def test_citation_cff():
    fixture = Path(__file__).parent / ".." / "CITATION.cff"
    file_contents = fixture.read_text(encoding="utf-8")
    actual_version = YAML(typ="safe").load(file_contents)["version"]
    assert actual_version == expected_version


def test_zenodo_json():
    fixture = Path(__file__).parent / ".." / ".zenodo.json"
    file_contents = fixture.read_text(encoding="utf-8")
    actual_version = json.loads(file_contents)["version"]
    assert actual_version == expected_version


def test_dockerfile():
    fixture = Path(__file__).parent / ".." / "Dockerfile"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^RUN .* cffconvert==(?P<version>\S*)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_alternative_install_options_md():
    fixture = Path(__file__).parent / ".." / "docs" / "alternative-install-options.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^docker build --tag cffconvert:(?P<version>\S*) .$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_1():
    fixture = Path(__file__).parent / ".." / "README.dev.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^# \(requires (?P<version>\S*) to be downloadable from PyPI\)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_2():
    fixture = Path(__file__).parent / ".." / "README.dev.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^docker build --tag cffconvert:(?P<version>\S*) .$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_readme_dev_md_3():
    fixture = Path(__file__).parent / ".." / "README.dev.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^docker tag cffconvert:(?P<version1>\S*) citationcff/" +
                       r"cffconvert:(?P<version2>\S*)$", re.MULTILINE)
    actual_version_1 = re.search(regex, file_contents)["version1"]
    actual_version_2 = re.search(regex, file_contents)["version2"]
    assert actual_version_1 == expected_version
    assert actual_version_2 == expected_version


def test_readme_dev_md_4():
    fixture = Path(__file__).parent / ".." / "README.dev.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"^docker push citationcff/cffconvert:(?P<version>\S*)$", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


def test_authors_keys_readme():
    fixture = Path(__file__).parent / ".." / "README.dev.md"
    file_contents = fixture.read_text(encoding="utf-8")
    regex = re.compile(r"blob/(?P<version>\S*)/cffconvert", re.MULTILINE)
    actual_version = re.search(regex, file_contents)["version"]
    assert actual_version == expected_version


expected_version = get_version_from_pyproject_toml()
