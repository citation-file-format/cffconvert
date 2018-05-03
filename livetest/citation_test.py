import unittest
import os
from cffconvert import Citation


class CitationTestUrlHasOrgRepoOnly(unittest.TestCase):

    def setUp(self):
        # https://github.com/<org>/<repo>
        url = "https://github.com/citation-file-format/cff-converter-python"
        self.citation = Citation(url=url)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
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
        fixture = os.path.join("fixtures", "1", "endnote.enw")
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


class CitationTestUrlHasOrgRepoTreeSha(unittest.TestCase):

    def setUp(self):
        # https://github.com/<org>/<repo>/tree/<sha>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/" + \
              "b7505591cf421ab33156ec0bffb0af43fd7d2cd1"
        self.citation = Citation(url=url)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
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
        fixture = os.path.join("fixtures", "1", "endnote.enw")
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


class CitationTestUrlHasOrgRepoOrgRepoTreeTag(unittest.TestCase):

    def setUp(self):
        # https://github.com/<org>/<repo>/tree/<tagname>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/0.0.1"
        self.citation = Citation(url=url)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
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
        fixture = os.path.join("fixtures", "1", "endnote.enw")
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


class CitationTestOrgRepoTreeBranch(unittest.TestCase):

    def setUp(self):
        # https://github.com/<org>/<repo>/tree/<branchname>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/master"
        self.citation = Citation(url=url)

    def test_printing_as_bibtex(self):
        fixture = os.path.join("fixtures", "1", "bibtex.bib")
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
        fixture = os.path.join("fixtures", "1", "endnote.enw")
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


class CitationTestInvalidInput(unittest.TestCase):

    def test_google(self):
        url = "www.google.com"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url=url)

        self.assertTrue("Only 'https://github.com' URLs are supported at the moment." == str(context.exception))

    def test_on_github_but_over_http(self):
        url = "http://github.com"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)

        self.assertTrue("Only 'https://github.com' URLs are supported at the moment." == str(context.exception))

    def test_on_github_but_no_org_specified(self):
        url = "https://github.com"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)

        self.assertTrue('Error extracting (user|organization) and/or repository ' +\
                        'information from the provided URL' in str(context.exception))

    def test_on_github_but_no_repo_specified(self):
        url = "https://github.com/citation-file-format"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)

        self.assertTrue('Error extracting (user|organization) and/or repository ' +\
                        'information from the provided URL' in str(context.exception))

    def test_on_github_but_repo_doesnt_exist(self):
        url = "https://github.com/ksjdnfjsnofiewdnodk28342u3842u304/ksdhjfjbsifasdibfasdf9090"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)

        self.assertTrue('Error requesting file: ' in str(context.exception))


if __name__ == "__main__":
    unittest.main()
