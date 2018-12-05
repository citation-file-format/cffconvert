import os
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
        self.assertEqual(result.output, "1.0.4\n")

    def test_printing_when_verbose(self):
        result = self.runner.invoke(cffconvert_cli, ["--verbose"])

        expected_output = ("{0} = {1}\n" +
                           "{2} = {3}\n" +
                           "{4} = {5}\n" +
                           "{6} = {7}\n" +
                           "{8} = {9}\n" +
                           "{10} = {11}\n" +
                           "{12} = {13}\n" +
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

    def test_local_cff_file_does_not_exist(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(cffconvert_cli, ["-f", "bibtex"])
        self.assertTrue(result.exit_code == -1)
        self.assertTrue(result.exception.strerror.startswith("No such file or directory"))


class CliTestsFromLocalCffFile(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_printing_as_bibtex_from_local_cff_file(self):
        fixture_bibtex = os.path.join("fixtures", "1", "bibtex.bib")
        with open(fixture_bibtex, "r") as f:
            expected_output = f.read() + "\n"

        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["-f", "bibtex"])
            actual_output = result.output

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_printing_as_codemeta_from_local_cff_file(self):
        fixture_codemeta = os.path.join("fixtures", "1", "codemeta.json")
        with open(fixture_codemeta, "r") as f:
            expected_output = f.read() + "\n"

        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["-f", "codemeta"])
            actual_output = result.output

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_printing_as_endnote_from_local_cff_file(self):
        fixture_endnote = os.path.join("fixtures", "1", "endnote.enw")
        with open(fixture_endnote, "r") as f:
            expected_output = f.read() + "\n"

        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["-f", "endnote"])
            actual_output = result.output

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_printing_as_ris_from_local_cff_file(self):
        fixture_ris = os.path.join("fixtures", "1", "ris.txt")
        with open(fixture_ris, "r") as f:
            expected_output = f.read() + "\n"

        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["-f", "ris"])
            actual_output = result.output

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_printing_as_zenodojson_from_local_cff_file(self):
        fixture_zenodo = os.path.join("fixtures", "1", "zenodo.json")
        with open(fixture_zenodo, "r") as f:
            expected_output = "Note: suspect keys will be included in the output.\n" + f.read() + "\n"

        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["-f", "zenodo"])
            actual_output = result.output

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_validating_a_local_valid_cff_file(self):
        fixture_cff = os.path.join("fixtures", "1", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["--validate"])
            actual_output = result.output

        expected_output = ""

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)

    def test_validating_a_local_invalid_cff_file(self):
        # this fixture has an invalid date (string instead of a Date object)
        fixture_cff = os.path.join("fixtures", "8", "CITATION.cff")
        with open(fixture_cff, "r") as f:
            cff_contents = f.read()

        with self.runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cff_contents)
            result = self.runner.invoke(cffconvert_cli, ["--validate"])
            actual_output = result.output

        # this is the feedback that pykwalifire gives when there is a date error:
        expected_output = "[\'%Y-%m-%d\']\n"

        self.assertTrue(result.exit_code == 0)
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
