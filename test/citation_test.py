import unittest
import os
import datetime
from cffconvert import Citation


class CitationTest1(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "citationcff-1")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-1")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-1")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-1")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-1")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTest2(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "citationcff-2")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-2")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-2")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-2")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-2")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTest3(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "citationcff-3")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-3")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-3")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-3")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-3")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTest4(unittest.TestCase):

    def setUp(self):
        url = "not used in unit testing"
        self.citation = Citation(url, instantiate_empty=True)
        fixture = os.path.join("fixtures", "citationcff-4")
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
        fixture = os.path.join("fixtures", "citationcff-1")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._override_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-5")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-5")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-5")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-5")
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
        fixture = os.path.join("fixtures", "citationcff-6")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-6-no-date")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-6-no-date")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-6-no-date")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-6-no-date")
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
        fixture = os.path.join("fixtures", "citationcff-6")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-6-no-doi")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-6-no-doi")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-6-no-doi")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-6-no-doi")
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
        fixture = os.path.join("fixtures", "citationcff-6")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-6-no-version")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-6-no-version")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-6-no-version")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-6-no-version")
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
        fixture = os.path.join("fixtures", "citationcff-1")
        with open(fixture) as f:
            self.citation.file_contents = f.read()
        self.citation.file_url = "not used in unit testing"
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "bibtex-1")
        with open(fixture) as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "codemeta-1")
        with open(fixture) as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "endnote-1")
        with open(fixture) as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "ris-1")
        with open(fixture) as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


if __name__ == "__main__":
    unittest.main()
