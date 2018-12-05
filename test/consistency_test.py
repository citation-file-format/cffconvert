import unittest
import os
import json
import ruamel.yaml as yaml
from cffconvert.version import __version__ as expected_version


class ConsistencyTests(unittest.TestCase):
    # These tests are included to check whether the version numbers are consistent across the various files (e.g.
    # cffvonvert/version.py, codemeta.json, .zenodo.json, CITATION.cff
    #
    # It also checks that version information, publication date, and doi have not accidentally been included in the
    # .zenodo.json file

    def setUp(self):
        # this uses the version information provided by the user through setup.py
        self.expected_version = expected_version

    def test_version_number_codemeta(self):
        # codemeta content should have the same semver as setup.py / version.py
        fixture = os.path.join("codemeta.json")
        with open(fixture, "r") as f:
            codemeta_contents = f.read()
        actual_version = json.loads(codemeta_contents)["version"]
        self.assertEqual(self.expected_version, actual_version)

    def test_version_number_cff(self):
        # CITATION.cff content should have the same semver as setup.py / version.py
        fixture = os.path.join("CITATION.cff")
        with open(fixture, "r") as f:
            cff_contents = f.read()
        actual_version = yaml.safe_load(cff_contents)["version"]
        self.assertEqual(self.expected_version, actual_version)

    def test_zenodo_has_no_version_number(self):
        # .zenodo.json content should not have any semver information, Zenodo retrieves this automatically from the
        # Zenodo-GtiHub integration
        fixture = os.path.join(".zenodo.json")
        with open(fixture, "r") as f:
            zenodojson_contents = f.read()
        self.assertFalse("version" in json.loads(zenodojson_contents).keys())

    def test_zenodo_has_no_doi(self):
        # .zenodo.json content should not have any doi information, Zenodo retrieves this automatically from the
        # Zenodo-GtiHub integration
        fixture = os.path.join(".zenodo.json")
        with open(fixture, "r") as f:
            zenodojson_contents = f.read()
        self.assertFalse("doi" in json.loads(zenodojson_contents).keys())

    def test_zenodo_has_no_date_published(self):
        # .zenodo.json content should not have any date information, Zenodo retrieves this automatically from the
        # Zenodo-GtiHub integration
        fixture = os.path.join(".zenodo.json")
        with open(fixture, "r") as f:
            zenodojson_contents = f.read()
        self.assertFalse("publication_date" in json.loads(zenodojson_contents).keys())


if __name__ == "__main__":
    unittest.main()
