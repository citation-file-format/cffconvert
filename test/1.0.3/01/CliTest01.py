import unittest
import os
from click.testing import CliRunner
from cffconvert import cli as cffconvert_cli


class CliTests(unittest.TestCase):

    @staticmethod
    def read_sibling_file(filename):
        f = os.path.join(os.path.dirname(__file__), filename)
        with open(f, "r") as f:
            return f.read()

    def test_local_cff_file_does_not_exist(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cffconvert_cli, ["-f", "bibtex"])
        self.assertTrue(result.exit_code == -1)
        self.assertTrue(result.exception.strerror.startswith("No such file or directory"))

    def test_printing_of_help(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cffconvert_cli, ["--help"])
        self.assertTrue(result.exit_code == 0)
        self.assertTrue(result.output[:6] == "Usage:")

    def test_printing_of_version(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cffconvert_cli, ["--version"])
        self.assertTrue(result.exit_code == 0)
        self.assertEqual(result.output, "1.4.0-alpha0\n")

    def test_printing_on_stdout_as_bibtex(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("bibtex.bib")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "bibtex"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_on_stdout_as_cff(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = cffstr
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "cff"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_on_stdout_as_codemeta(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("codemeta.json")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "codemeta"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_on_stdout_as_endnote(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("endnote.enw")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "endnote"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_on_stdout_as_ris(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("ris.txt")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "ris"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_on_stdout_as_schemaorg(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("schemaorg.json")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "schema.org"])
        self.assertEqual(result.exit_code, 0)
        actual = result.output
        self.assertEqual(expected, actual)

    def test_printing_when_verbose(self):
        expected_output = ("{0} = {1}\n" +
                           "{2} = {3}\n" +
                           "{4} = {5}\n" +
                           "{6} = {7}\n" +
                           "{8} = {9}\n" +
                           "{10} = {11}\n" +
                           "{12} = {13}\n" +
                           "{14} = {15}\n").format("infile", None,
                                                   "outfile", None,
                                                   "outputformat", None,
                                                   "url", None,
                                                   "validate", False,
                                                   "ignore_suspect_keys", False,
                                                   "verbose", True,
                                                   "version", False)
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cffconvert_cli, ["--verbose"])
        self.assertTrue(result.exit_code == -1)
        self.assertEqual(result.output, expected_output)

    def test_raising_valueerror_on_unsupported_format(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "unsupported_97491"])
        self.assertEqual(result.exit_code, -1)
        self.assertTrue(isinstance(result.exception, ValueError))
        self.assertTrue(str(result.exception).startswith('\'--outputformat\' should be one of ['))

    def test_without_arguments(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cffconvert_cli, [])
        self.assertTrue(result.exit_code == -1)
        self.assertTrue(isinstance(result.exception, FileNotFoundError))
        self.assertEqual(result.exception.strerror, 'No such file or directory')

    def test_writing_as_bibtex(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("bibtex.bib")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "bibtex",
                                                         "--outfile", "bibtex.bib"])
            with open("bibtex.bib", "r") as f:
                actual = f.read()
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(expected, actual)

    def test_writing_as_codemeta(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("codemeta.json")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "codemeta",
                                                         "--outfile", "codemeta.json"])
            with open("codemeta.json", "r") as f:
                actual = f.read()
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(expected, actual)

    def test_writing_as_endnote(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("endnote.enw")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "endnote",
                                                         "--outfile", "endnote.enw"])
            with open("endnote.enw", "r") as f:
                actual = f.read()
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(expected, actual)

    def test_writing_as_ris(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("ris.txt")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "ris",
                                                         "--outfile", "ris.txt"])
            with open("ris.txt", "r") as f:
                actual = f.read()
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(expected, actual)

    def test_writing_as_schemaorg(self):
        cffstr = CliTests.read_sibling_file("CITATION.cff")
        expected = CliTests.read_sibling_file("schemaorg.json")
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open("CITATION.cff", "w") as f:
                f.write(cffstr)
            result = runner.invoke(cffconvert_cli, ["--outputformat", "schema.org",
                                                         "--outfile", "schemaorg.json"])
            with open("schemaorg.json", "r") as f:
                actual = f.read()
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()








