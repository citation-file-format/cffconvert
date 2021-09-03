# `cffconvert`

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1162057.svg)](https://doi.org/10.5281/zenodo.1162057)
[![Travis build status](https://travis-ci.org/citation-file-format/cff-converter-python.svg?branch=master)](https://travis-ci.org/citation-file-format/cff-converter-python)
[![SonarCloud Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=citation-file-format_cff-converter-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=citation-file-format_cff-converter-python)
[![PyPi Badge](https://img.shields.io/pypi/v/cffconvert.svg?colorB=blue)](https://pypi.python.org/pypi/cffconvert/)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1811/badge)](https://bestpractices.coreinfrastructure.org/projects/1811)
[![Research Software Directory](https://img.shields.io/badge/rsd-cffconvert-00a3e3.svg)](https://www.research-software.nl/software/cff-converter-python)
[![fair-software.eu](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green)](https://fair-software.eu)

Command line program to validate and convert [`CITATION.cff`](https://github.com/citation-file-format/citation-file-format) files.

Supported input versions of the Citation File Format:

| Citation File Format schema version | Link to Zenodo release |
| --- | --- |
| `1.2.0` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5171937.svg)](https://doi.org/10.5281/zenodo.5171937) |
| `1.1.0` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4813122.svg)](https://doi.org/10.5281/zenodo.4813122) |
| `1.0.3` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1222163.svg)](https://doi.org/10.5281/zenodo.1222163) |
| `1.0.2` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1120256.svg)](https://doi.org/10.5281/zenodo.1120256) |
| `1.0.1` | [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1117789.svg)](https://doi.org/10.5281/zenodo.1117789) |

Supported output formats:

1.  BibTeX
1.  CodeMeta
1.  EndNote
1.  JSON
1.  plaintext APA
1.  RIS
1.  schema.org JSON
1.  Zenodo JSON

<!--
Besides local files, `cffconvert` can fetch `CITATION.cff` file contents from the following GitHub URLs:

1.  `https://github.com/<org>/<repo>`
2.  `https://github.com/<org>/<repo>/tree/<sha>`
3.  `https://github.com/<org>/<repo>/tree/<tagname>`
4.  `https://github.com/<org>/<repo>/tree/<branchname>`
-->

`cffconvert` does not aim to support the full Citation File Format specification.

## Installing

To install in user space, 

```shell
python3 -m pip install --user cffconvert
```
Ensure that the user space directory `~/.local/bin/` is on the `PATH`.

```shell
which cffconvert
```
should now return the location of the program.

See [docs/alternative-install-options.md](docs/alternative-install-options.md) for alternative install options.

## Command line interface

See `cffconvert`'s options:

```shell
cffconvert --help
```

Shows:

```shell
Usage: cffconvert [OPTIONS]

Options:
  -i PATH                         Path to the CITATION.cff input file. Default
                                  value is './CITATION.cff'.
  -o PATH                         Path to the output file.
  -f [apalike|bibtex|cff|codemeta|endnote|ris|schema.org|zenodo]
                                  Output format.
  -h, --help                      Show help and exit.
  --show-trace                    Show error trace.
  --validate                      Validate the CITATION.cff and exit.
  --ignore-suspect-keys           Ignore any keys from CITATION.cff that are
                                  likely out of date, such as 'commit', 'date-
                                  released', 'doi', and 'version'.
  --verbose                       Provide feedback on what was entered.
  --version                       Print version and exit.
```

## Example usage

### Validating

```shell
cffconvert --validate
cffconvert --validate -i CITATION.cff
cffconvert --validate -i ${PWD}/CITATION.cff
cffconvert --validate -i ../some-other-dir/CITATION.cff
```

### Converting metadata to other formats

If there is a valid CITATION.cff file in the current directory, you can convert to various other formats and 
print the result on standard out with:

```shell
cffconvert -f bibtex
cffconvert -f codemeta
cffconvert -f endnote
cffconvert -f ris
cffconvert -f schema.org
cffconvert -f zenodo
cffconvert -f apalike
```

### Writing to a file

```shell
# with i/o redirection:
cffconvert -f bibtex > bibtex.bib
cffconvert -f zenodo > zenodo.json
cffconvert -f endnote > ${PWD}/endnote.enw
# etc

# without i/o redirection
cffconvert -f bibtex -o bibtex.bib
cffconvert -f zenodo -o zenodo.json
cffconvert -f endnote -o ${PWD}/endnote.enw
# etc
```
