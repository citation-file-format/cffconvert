[![Build Status](https://travis-ci.org/citation-file-format/cff-converter-python.svg?branch=master)](https://travis-ci.org/citation-file-format/cff-converter-python)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1162057.svg)](https://doi.org/10.5281/zenodo.1162057)
[![Research Software Directory](https://img.shields.io/badge/rsd-cff--converter--python-00a3e3.svg)](https://www.research-software.nl/software/cff-converter-python)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1811/badge)](https://bestpractices.coreinfrastructure.org/projects/1811)

# cffconvert

Read [CFF formatted CITATION](https://github.com/citation-file-format) file from a GitHub
url and convert it to various formats, such as:

1. BibTeX
1. EndNote
1. RIS
1. codemeta
1. plain JSON
1. Zenodo JSON

Supported types of GitHub URL:

1. ``https://github.com/<org>/<repo>``
1. ``https://github.com/<org>/<repo>/tree/<sha>``
1. ``https://github.com/<org>/<repo>/tree/<tagname>``
1. ``https://github.com/<org>/<repo>/tree/<branchname>``

``cffconvert`` does not support the full
[CFF spec](https://citation-file-format.github.io/assets/pdf/cff-specifications-1.0.3.pdf) yet.



# For users

## Install

```bash
pip install git+https://github.com/citation-file-format/cff-converter-python.git
```

# For developers

## Install

```bash
# get a copy of the cff-converter-python software
git clone https://github.com/citation-file-format/cff-converter-python.git
# change directory into cff-converter-python
cd cff-converter-python
# make a Python3.5 virtual environment named .venv35
virtualenv -p /usr/bin/python3.5 .venv35
# activate the virtual environment
source ./.venv35/bin/activate
# install any packages that cff-converter-python needs
pip install -r requirements.txt
```


## Running tests

```bash
# (from the project root)

# run unit tests
pytest test/

# run tests against live system (GitHub)
pytest livetest/
```
