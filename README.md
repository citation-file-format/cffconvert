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

- `1.1.0` [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4813122.svg)](https://doi.org/10.5281/zenodo.4813122)
- `1.0.3` [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1222163.svg)](https://doi.org/10.5281/zenodo.1222163)
- `1.0.2` [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1120256.svg)](https://doi.org/10.5281/zenodo.1120256)
- `1.0.1` [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1117789.svg)](https://doi.org/10.5281/zenodo.1117789)

Supported output formats:

1.  BibTeX
1.  CodeMeta
1.  EndNote
1.  JSON
1.  plaintext APA
1.  RIS
1.  schema.org JSON
1.  Zenodo JSON

Besides local files, `cffconvert` can fetch `CITATION.cff` file contents from the following GitHub URLs:

1.  `https://github.com/<org>/<repo>`
2.  `https://github.com/<org>/<repo>/tree/<sha>`
3.  `https://github.com/<org>/<repo>/tree/<tagname>`
4.  `https://github.com/<org>/<repo>/tree/<branchname>`

`cffconvert` does not aim to support the full Citation File Format specification.

## Installing `cffconvert` in user space

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
  -if, --infile TEXT          Path to the CITATION.cff input file. Use '--infile -' to read from STDIN.
  -of, --outfile TEXT         Path to the output file.
  -f, --outputformat TEXT     Output format: bibtex|cff|codemeta|endnote|ris|schema.org|zenodo
  -u, --url TEXT              URL of the repo containing the CITATION.cff (currently only github.com is supported; may
                              include branch name, commit sha, tag name). For example: 'https://github.com/citation-
                              file-format/cff-converter-python' or 'https://github.com/citation-file-format/cff-
                              converter-python/tree/master'
  --validate                  Validate the CITATION.cff found at the URL or supplied through '--infile'
  -ig, --ignore-suspect-keys  If True, ignore any keys from CITATION.cff that are likely out of date, such as
                              'commit', 'date-released', 'doi', and 'version'.
  --verbose                   Provide feedback on what was entered.
  --version                   Print version and exit.
  --help                      Show this message and exit.
```

## Example usage

### Convert local `CITATION.cff` to BibTeX

Assume you have a local `CITATION.cff` file with the following contents:

```yaml
authors:
  - family-names: Spaaks
    given-names: "Jurriaan H."
cff-version: 1.1.0
date-released: 2019-11-12
doi: 10.5281/zenodo.1162057
message: "If you use this software, please cite it using these metadata."
repository-code: "https://github.com/citation-file-format/cff-converter-python"
title: cffconvert
version: 1.3.3
```

These metadata can be converted to BibTeX using:

```
cffconvert -f bibtex
```

Which results in:

```bibtex
@misc{YourReferenceHere,
author = {
            Jurriaan H. Spaaks
         },
title  = {cffconvert},
month  = {11},
year   = {2019},
doi    = {10.5281/zenodo.1162057},
url    = {https://github.com/citation-file-format/cff-converter-python}
}
```

### Retrieve `CITATION.cff` contents from a URL, output as `codemeta.json`

`cffconvert` can retrieve the contents of a `CITATION.cff` file, if the file is in a public repository on GitHub, as follows:

```shell
cffconvert -f codemeta \
--url https://github.com/citation-file-format/cff-converter-python/tree/1.3.3 > codemeta.json
```

Contents of file `codemeta.json`:

```json
{
   "@context": "https://doi.org/10.5063/schema/codemeta-2.0", 
   "@type": "SoftwareSourceCode", 
   "author": [
      {
         "@id": "https://orcid.org/0000-0002-7064-4069", 
         "@type": "Person", 
         "affiliation": {
            "@type": "Organization", 
            "legalName": "Netherlands eScience Center"
         }, 
         "familyName": "Spaaks", 
         "givenName": "Jurriaan H."
      }, 
      {
         "@type": "Person", 
         "affiliation": {
            "@type": "Organization", 
            "legalName": "Netherlands eScience Center"
         }, 
         "familyName": "Klaver", 
         "givenName": "Tom"
      }, 
      {
         "@id": "https://orcid.org/0000-0002-5821-2060", 
         "@type": "Person", 
         "affiliation": {
            "@type": "Organization", 
            "legalName": "Netherlands eScience Center"
         }, 
         "familyName": "Verhoeven", 
         "givenName": "Stefan"
      }, 
      {
         "@id": "https://orcid.org/0000-0003-4925-7248", 
         "@type": "Person", 
         "affiliation": {
            "@type": "Organization", 
            "legalName": "Humboldt-Universität zu Berlin"
         }, 
         "familyName": "Druskat", 
         "givenName": "Stephan"
      }
   ], 
   "codeRepository": "https://github.com/citation-file-format/cff-converter-python", 
   "datePublished": "2019-11-12", 
   "description": "Command line program to convert from Citation File Format to various other formats such as BibTeX, EndNote, RIS, schema.org, and .zenodo.json.", 
   "identifier": "https://doi.org/10.5281/zenodo.1162057", 
   "keywords": [
      "citation", 
      "bibliography", 
      "cff", 
      "CITATION.cff"
   ], 
   "license": "https://spdx.org/licenses/Apache-2.0", 
   "name": "cffconvert", 
   "version": "1.3.3"
}
```
### Local `CITATION.cff` to Zenodo metadata file

Convert the contents of a local file `CITATION.cff` into the format used by `.zenodo.json` files (see [Zenodo's API
docs](http://developers.zenodo.org/#representation)), while ignoring any keys that are likely out of date:

```shell
cffconvert -f zenodo --ignore-suspect-keys
```

Results in (note absence of `date-released`, `doi`, and `version`):

```json
{
    "creators": [
        {
            "affiliation": "Netherlands eScience Center",
            "name": "Spaaks, Jurriaan H."
        },
        {
            "affiliation": "Netherlands eScience Center",
            "name": "Klaver, Tom"
        },
        {
            "affiliation": "Netherlands eScience Center",
            "name": "Verhoeven, Stefan"
        }
    ],
    "keywords": [
        "citation",
        "bibliography",
        "cff",
        "CITATION.cff"
    ],
    "license": {
        "id": "Apache-2.0"
    },
    "title": "cffconvert"
}
```
