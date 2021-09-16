import json
import os
import re
from ruamel.yaml import YAML
from cffconvert.version import __version__ as expected_version
from cffconvert.root import get_package_root


def test_citation_cff():
    fixture = os.path.join(get_package_root(), "..", "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    actual_version = YAML(typ='safe').load(file_contents)["version"]
    assert actual_version == expected_version


def test_zenodo_json():
    fixture = os.path.join(get_package_root(), "..", ".zenodo.json")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    actual_version = json.loads(file_contents)["version"]
    assert actual_version == expected_version


def test_dockerfile():
    fixture = os.path.join(get_package_root(), "..", "Dockerfile")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^RUN .* cffconvert==(?P<version>\S*)$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_setup_cfg():
    fixture = os.path.join(get_package_root(), "..", "setup.cfg")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^version = (?P<version>\S*)$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_alternative_install_options_md():
    fixture = os.path.join(get_package_root(), "..", "docs", "alternative-install-options.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^docker build --tag cffconvert:(?P<version>\S*) .$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_test_1_0_3__01_cli_py():
    fixture = os.path.join(get_package_root(), "..", "test", "1.0.3", "01", "test_1_0_3__01_cli.py")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^[ ]{4}assert result\.output == "(?P<version>\S*)\\n"$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_test_1_1_0__01_cli_py():
    fixture = os.path.join(get_package_root(), "..", "test", "1.1.0", "01", "test_1_1_0__01_cli.py")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^[ ]{4}assert result\.output == "(?P<version>\S*)\\n"$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_1_2_0_doi_identifiers_d__cli_py():
    fixture = os.path.join(get_package_root(), "..", "test", "1.2.0", "doi-identifiers", "D_",
                           "test_1_2_0_doi_identifiers_D__cli.py")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^[ ]{4}assert result\.output == "(?P<version>\S*)\\n"$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_readme_dev_md_1():
    fixture = os.path.join(get_package_root(), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^# \(requires (?P<version>\S*) to be downloadable from PyPI\)$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_readme_dev_md_2():
    fixture = os.path.join(get_package_root(), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^docker build --tag cffconvert:(?P<version>\S*) .$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version


def test_readme_dev_md_3():
    fixture = os.path.join(get_package_root(), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^docker tag cffconvert:(?P<version1>\S*) citationcff/' +
                       r'cffconvert:(?P<version2>\S*)$', re.MULTILINE)
    actual_version_1 = re.search(regex, file_contents)['version1']
    actual_version_2 = re.search(regex, file_contents)['version2']
    assert actual_version_1 == expected_version
    assert actual_version_2 == expected_version


def test_readme_dev_md_4():
    fixture = os.path.join(get_package_root(), "..", "README.dev.md")
    with open(fixture, "rt", encoding="utf-8") as fid:
        file_contents = fid.read()
    regex = re.compile(r'^docker push citationcff/cffconvert:(?P<version>\S*)$', re.MULTILINE)
    actual_version = re.search(regex, file_contents)['version']
    assert actual_version == expected_version
