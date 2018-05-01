import unittest
import os
import datetime
from cffconvert import Citation


class CitationTest1(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "1", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "1", "endnote.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "1", "zenodo.json")
        with open(fixture) as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest2(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "2", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "2", "bibtex.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "2", "codemeta.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "2", "endnote.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "2", "ris.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "2", "zenodo.json")
        with open(fixture) as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest3(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "3", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "3", "bibtex.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "3", "codemeta.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "3", "endnote.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "3", "ris.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "3", "zenodo.json")
        with open(fixture) as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest4(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "4", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"

    def test_conversion_to_yaml(self):
        with self.assertRaises(Exception) as context:
            self.citation._parse_yaml()

        self.assertTrue('Provided CITATION.cff does not seem valid YAML.' in str(context.exception))


class CitationTestOverride(unittest.TestCase):

    def setUp(self):
        # with override
        url = "not used in unit testing"
        override = {
            "doi": "thebestdoi.23678237",
            "date-released": datetime.datetime.strptime("2018-03-05", "%Y-%m-%d").date()
        }
        self.citation = Citation(url, instantiate_empty=True, override=override)
        fixture = os.path.join("fixtures", "1", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._override_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "5", "bibtex.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "5", "codemeta.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "5", "endnote.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "5", "ris.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyDate(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "date-released"
        url = "not used in unit testing"
        remove = ["date-released"]
        self.citation = Citation(url, instantiate_empty=True, remove=remove)
        fixture = os.path.join("fixtures", "6", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-date.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-date.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-date.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-date.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyDoi(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "doi"
        url = "not used in unit testing"
        remove = ["doi"]
        self.citation = Citation(url, instantiate_empty=True, remove=remove)
        fixture = os.path.join("fixtures", "6", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-doi.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-doi.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-doi.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-doi.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyVersion(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "version"
        url = "not used in unit testing"
        remove = ["version"]
        self.citation = Citation(url, instantiate_empty=True, remove=remove)
        fixture = os.path.join("fixtures", "6", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-version.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-version.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-version.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-version.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveNonExistentKey(unittest.TestCase):

    def setUp(self):
        # trying to remove a key that doesn't exist
        url = "not used in unit testing"
        remove = ["hjjshbdjsu3933"]
        self.citation = Citation(url, instantiate_empty=True, remove=remove)
        fixture = os.path.join("fixtures", "1", "citation.cff")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.txt")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "1", "endnote.txt")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


if __name__ == "__main__":
    unittest.main()
