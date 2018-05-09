import unittest
from click.testing import CliRunner
from cffconvert import cli as cffconvert_cli


class CliTests(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.defaults = {
            "infile": None,
            "outfile": None,
            "outputformat": None,
            "url": None,
            "validate": False,
            "ignore_suspect_keys": False,
            "version": False
        }

    def test_without_arguments(self):
        result = self.runner.invoke(cffconvert_cli, [])
        self.assertTrue(result.exit_code == -1)
        self.assertTrue(str(result.exception).startswith("'--outputformat' should be one of "))

    def test_printing_of_help(self):
        result = self.runner.invoke(cffconvert_cli, ["--help"])
        self.assertTrue(result.exit_code == 0)
        self.assertTrue(result.output[:6] == "Usage:")

    def test_printing_of_version(self):
        result = self.runner.invoke(cffconvert_cli, ["--version"])
        self.assertTrue(result.exit_code == 0)
        self.assertEqual(result.output, "0.0.4\n")

    def test_printing_of_verbose(self):
        result = self.runner.invoke(cffconvert_cli, ["--verbose"])

        expected_output = ("{0} = {1}\n" +\
                           "{2} = {3}\n" +\
                           "{4} = {5}\n" +\
                           "{6} = {7}\n" +\
                           "{8} = {9}\n" +\
                           "{10} = {11}\n" + \
                           "{12} = {13}\n" + \
                           "{14} = {15}\n").format("infile", self.defaults["infile"],
                                                   "outfile", self.defaults["outfile"],
                                                   "outputformat", self.defaults["outputformat"],
                                                   "url", self.defaults["url"],
                                                   "validate", self.defaults["validate"],
                                                   "ignore_suspect_keys", self.defaults["ignore_suspect_keys"],
                                                   "verbose", True,
                                                   "version", self.defaults["version"])
        self.assertTrue(result.exit_code == -1)
        self.assertEqual(result.output, expected_output)



if __name__ == "__main__":
    unittest.main()
