import os
from click.testing import CliRunner
from cffconvert import cli as cffconvert_cli


def read_sibling_file(filename):
    f = os.path.join(os.path.dirname(__file__), filename)
    with open(f, "r") as f:
        return f.read()


def test_local_cff_file_does_not_exist():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cffconvert_cli, ["-f", "bibtex"])
    assert result.exit_code == 1
    assert result.exception.strerror.startswith("No such file or directory")


def test_printing_of_help():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cffconvert_cli, ["--help"])
    assert result.exit_code == 0
    assert result.output[:6] == "Usage:"


def test_printing_of_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cffconvert_cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == "2.0.0-alpha.0\n"


def test_printing_on_stdout_as_bibtex():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("bibtex.bib")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "bibtex"])
    assert result.exit_code == 0
    actual = result.output
    assert expected == actual


def test_printing_on_stdout_as_cff():
    cffstr = read_sibling_file("CITATION.cff")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "cff"])
    assert result.exit_code == 0
    assert cffstr == result.output


def test_printing_on_stdout_as_codemeta():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("codemeta.json")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "codemeta"])
    assert result.exit_code == 0
    actual = result.output
    assert expected == actual


def test_printing_on_stdout_as_endnote():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("endnote.enw")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "endnote"])
    assert result.exit_code == 0
    actual = result.output
    assert expected == actual


def test_printing_on_stdout_as_ris():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("ris.txt")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "ris"])
    assert result.exit_code == 0
    actual = result.output
    assert expected == actual


def test_printing_on_stdout_as_schemaorg():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("schemaorg.json")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "schema.org"])
    assert result.exit_code == 0
    actual = result.output
    assert expected == actual


def test_printing_when_verbose():
    expected_output = ("infile = None\n" +
                       "outfile = None\n" +
                       "outputformat = None\n" +
                       "url = None\n" +
                       "show_help = False\n" +
                       "show_trace = False\n" +
                       "validate = False\n" +
                       "ignore_suspect_keys = False\n" +
                       "verbose = True\n" +
                       "version = False\n")
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cffconvert_cli, ["--verbose"])
    assert result.exit_code == 1
    assert result.output == expected_output


def test_raising_error_on_unsupported_format():
    cffstr = read_sibling_file("CITATION.cff")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "unsupported_97491"])
    assert result.exit_code == 2
    assert "Error: Invalid value for '-f'" in str(result.output)


def test_without_arguments():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cffconvert_cli, [])
    assert result.exit_code == 1
    assert isinstance(result.exception, FileNotFoundError)
    assert result.exception.strerror == 'No such file or directory'


def test_writing_as_bibtex():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("bibtex.bib")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "bibtex", "-o", "bibtex.bib"])
        with open("bibtex.bib", "r") as f:
            actual = f.read()
    assert result.exit_code == 0
    assert expected == actual


def test_writing_as_codemeta():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("codemeta.json")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "codemeta", "-o", "codemeta.json"])
        with open("codemeta.json", "r") as f:
            actual = f.read()
    assert result.exit_code == 0
    assert expected == actual


def test_writing_as_endnote():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("endnote.enw")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "endnote", "-o", "endnote.enw"])
        with open("endnote.enw", "r") as f:
            actual = f.read()
    assert result.exit_code == 0
    assert expected == actual


def test_writing_as_ris():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("ris.txt")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "ris", "-o", "ris.txt"])
        with open("ris.txt", "r") as f:
            actual = f.read()
    assert result.exit_code == 0
    assert expected == actual


def test_writing_as_schemaorg():
    cffstr = read_sibling_file("CITATION.cff")
    expected = read_sibling_file("schemaorg.json")
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("CITATION.cff", "w") as f:
            f.write(cffstr)
        result = runner.invoke(cffconvert_cli, ["-f", "schema.org", "-o", "schemaorg.json"])
        with open("schemaorg.json", "r") as f:
            actual = f.read()
    assert result.exit_code == 0
    assert expected == actual
