import unittest
from cffconvert import Citation


class CitationTestInvalidInput(unittest.TestCase):

    def test_google(self):
        url = "www.google.com"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url=url)
        self.assertTrue("Only 'https://github.com' URLs are supported at the moment." == str(context.exception))

    def test_on_github_but_no_org_specified(self):
        url = "https://github.com"
        with self.assertRaises(ValueError) as context:
            self.citation = Citation(url)
        self.assertTrue('Error extracting (user|organization) and/or repository ' +\
                        'information from the provided URL' in str(context.exception))

    def test_on_github_but_no_repo_specified(self):
        url = "https://github.com/citation-file-format"
        with self.assertRaises(ValueError) as context:
            self.citation = Citation(url)
        self.assertTrue('Error extracting (user|organization) and/or repository ' +\
                        'information from the provided URL' in str(context.exception))

    def test_on_github_but_over_http(self):
        url = "http://github.com"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)
        self.assertTrue("Only 'https://github.com' URLs are supported at the moment." == str(context.exception))

    def test_on_github_but_repo_doesnt_exist(self):
        url = "https://github.com/org_1122334455/repo_0123456789"
        with self.assertRaises(Exception) as context:
            self.citation = Citation(url)
        self.assertTrue('Error requesting file: ' in str(context.exception))

    def test_on_github_with_url_without_tree_element(self):
        url = "https://github.com/xenon-middleware/xenon/sha/134624562456"
        with self.assertRaises(ValueError) as context:
            self.citation = Citation(url)
        self.assertTrue(str(context.exception).startswith("Expected 'https://github.com/" +
                        "<org>/<repo>/tree/...' but instead found"))


if __name__ == "__main__":
    unittest.main()
