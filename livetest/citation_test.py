import unittest
import os
from cffconvert import Citation


class CitationTestUrlHasOrgRepoOnly(unittest.TestCase):

    def test_retrieval_of_latest_master(self):
        # this test checks if cffconvert can behave similar to a simple curl or wget
        # https://github.com/<org>/<repo>
        url = "https://github.com/citation-file-format/cff-converter-python"
        citation = Citation(url=url)
        self.assertNotEqual(citation, None)


class CitationTestUrlHasOrgRepoTreeSha(unittest.TestCase):

    def test_retrieval_via_sha(self):
        # https://github.com/<org>/<repo>/tree/<sha>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/" + \
              "b7505591cf421ab33156ec0bffb0af43fd7d2cd1"
        citation = Citation(url=url)
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture) as f:
            expected_cffstr = f.read()
        actual_cffstr = citation.cffstr
        self.assertEqual(expected_cffstr, actual_cffstr)


class CitationTestUrlHasOrgRepoOrgRepoTreeTag(unittest.TestCase):

    def test_retrieval_via_tag(self):
        # https://github.com/<org>/<repo>/tree/<tagname>
        url = "https://github.com/citation-file-format/cff-converter-python/tree/0.0.1"
        citation = Citation(url=url)
        fixture = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture) as f:
            expected_cffstr = f.read()
        actual_cffstr = citation.cffstr
        self.assertEqual(expected_cffstr, actual_cffstr)


class CitationTestOrgRepoTreeBranch(unittest.TestCase):

    def test_retrieval_via_branchname(self):
        # https://github.com/<org>/<repo>/tree/<branchname>
        # this test checks if cffconvert can behave similar to a simple curl or wget
        url = "https://github.com/citation-file-format/cff-converter-python/tree/master"
        citation = Citation(url=url)
        self.assertNotEqual(citation, None)


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
