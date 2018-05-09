import unittest
import os
import datetime
from cffconvert import Citation


class CitationTest1(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, suspect_keys=[])

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "1", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "1", "zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest2(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join("fixtures", "2", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, suspect_keys=[])

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "2", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "2", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "2", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "2", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "2", "zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest3(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join("fixtures", "3", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, suspect_keys=[])

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "3", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "3", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "3", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "3", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)

    def test_printing_as_zenodojson(self):
        fixture = os.path.join("fixtures", "3", "zenodo.json")
        with open(fixture, "r") as f:
            expected_zenodojson = f.read()
        actual_zenodojson = self.citation.as_zenodojson()
        self.assertEqual(expected_zenodojson, actual_zenodojson)


class CitationTest4(unittest.TestCase):

    def setUp(self):
        fixture = os.path.join("fixtures", "4", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True)

    def test_conversion_to_yaml(self):
        with self.assertRaises(ValueError) as context:
            self.citation._parse_yaml()

        self.assertTrue('Provided CITATION.cff does not seem valid YAML.' in str(context.exception))


class CitationTestOverride(unittest.TestCase):

    def setUp(self):
        # with override
        override = {
            "doi": "thebestdoi.23678237",
            "date-released": datetime.datetime.strptime("2018-03-05", "%Y-%m-%d").date()
        }
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True, override=override)
        self.citation._parse_yaml()
        self.citation._override_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "5", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "5", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "5", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "5", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyDate(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "date-released"
        remove = ["date-released"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True, remove=remove)
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-date.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-date.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-date.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-date.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestIgnoreSuspectKeyDate(unittest.TestCase):

    def setUp(self):
        # ignore suspect key "date-released"
        suspect_keys = ["date-released"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, ignore_suspect_keys=True, suspect_keys=suspect_keys)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-date.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-date.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-date.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-date.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyDoi(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "doi"
        remove = ["doi"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True, remove=remove)
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-doi.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-doi.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-doi.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-doi.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestIgnoreSuspectKeyDoi(unittest.TestCase):

    def setUp(self):
        # ignore suspect key "doi"
        suspect_keys = ["doi"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, ignore_suspect_keys=True, suspect_keys=suspect_keys)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-doi.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-doi.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-doi.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-doi.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveSuspectKeyVersion(unittest.TestCase):

    def setUp(self):
        # with removal of suspect key "version"
        remove = ["version"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True, remove=remove)
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-version.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-version.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-version.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-version.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestIgnoreSuspectKeyVersion(unittest.TestCase):

    def setUp(self):
        # ignore suspect key "version"
        suspect_keys = ["version"]
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, ignore_suspect_keys=True, suspect_keys=suspect_keys)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-version.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-version.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-version.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-version.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestIgnoreAllSuspectKeys(unittest.TestCase):

    def setUp(self):
        # ignore all suspect keys
        fixture = os.path.join("fixtures", "6", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, ignore_suspect_keys=True)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "6", "bibtex-no-suspect-keys.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "6", "codemeta-no-suspect-keys.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "6", "endnote-no-suspect-keys.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "6", "ris-no-suspect-keys.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestRemoveNonExistentKey(unittest.TestCase):

    def setUp(self):
        # trying to remove a key that doesn't exist
        remove = ["hjjshbdjsu3933"]
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, instantiate_empty=True, remove=remove)
        self.citation._parse_yaml()
        self.citation._remove_suspect_keys()

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "1", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestIgnoreNonExistentKey(unittest.TestCase):

    def setUp(self):
        # trying to ignore a key that doesn't exist
        suspect_keys = ["hjjshbdjsu3933"]
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
        self.citation = Citation(cffstr=cffstr, ignore_suspect_keys=True, suspect_keys=suspect_keys)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
        with open(fixture, "r") as f:
            expected_bibtex = f.read()
        actual_bibtex = self.citation.as_bibtex()
        self.assertEqual(expected_bibtex, actual_bibtex)

    def test_printing_as_codemeta(self):
        fixture = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture, "r") as f:
            expected_codemeta = f.read()
        actual_codemeta = self.citation.as_codemeta()
        self.assertEqual(expected_codemeta, actual_codemeta)

    def test_printing_as_enw(self):
        fixture = os.path.join("fixtures", "1", "endnote.enw")
        with open(fixture, "r") as f:
            expected_endnote = f.read()
        actual_endnote = self.citation.as_enw()
        self.assertEqual(expected_endnote, actual_endnote)

    def test_printing_as_ris(self):
        fixture = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture, "r") as f:
            expected_ris = f.read()
        actual_ris = self.citation.as_ris()
        self.assertEqual(expected_ris, actual_ris)


class CitationTestXorUrlCffstr(unittest.TestCase):

    def test_both_url_and_cffstr(self):
        with self.assertRaises(ValueError) as context:
            self.citation = Citation(url="some url", cffstr="some cffstr")
        assert "You should specify either \'url\' or \'cffstr\'." in str(context.exception)

    def test_neither_url_nor_cffstr(self):
        with self.assertRaises(ValueError):
            self.citation = Citation()


if __name__ == "__main__":
    unittest.main()
