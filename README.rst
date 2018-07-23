Badges
======

- |Zenodo DOI|
- |Travis build status|
- |PyPI badge|
- |CII Best Practices|
- |SonarCloud Quality Gate|
- |SonarCloud Code Coverage|
- |Research Software Directory|

cffconvert
==========

Read `CFF formatted
CITATION <https://github.com/citation-file-format>`__ file from a GitHub
url and convert it to various formats, such as:

1. BibTeX
2. EndNote
3. RIS
4. codemeta
5. plain JSON
6. Zenodo JSON

Supported types of GitHub URL:

1. ``https://github.com/<org>/<repo>``
2. ``https://github.com/<org>/<repo>/tree/<sha>``
3. ``https://github.com/<org>/<repo>/tree/<tagname>``
4. ``https://github.com/<org>/<repo>/tree/<branchname>``

``cffconvert`` does not support the full `CFF
spec <https://citation-file-format.github.io/assets/pdf/cff-specifications-1.0.3.pdf>`__
yet.

For users
=========

Install
-------

There are a few options:

**Option 1 (preferred): install in user space.**

Ensure that the user space directory ``~/.local/bin/`` is on the ``PATH``.

.. code:: bash

    pip3 install --user cffconvert


**Option 2 (not preferred): install in virtual environment**

.. code:: bash

    virtualenv -p /usr/bin/python3.5 myvenv3
    source myvenv3/bin/activate
    pip3 install cffconvert

**Option 3 (not preferred): install globally**

Note: this option needs sudo rights.

.. code:: bash

    sudo -H pip3 install cffconvert

**Option 4 (not preferred): install with conda**

See https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment

.. code:: bash

    conda install pip
    pip install cffconvert


Command line interface
----------------------

See ``cffconvert``'s options:

.. code:: bash

    cffconvert --help

Shows:

.. code:: bash

    Usage: cffconvert [OPTIONS]

    Options:
      -if, --infile TEXT          Path to the CITATION.cff input file.
      -of, --outfile TEXT         Path to the output file.
      -f, --outputformat TEXT     Output format: bibtex|cff|codemeta|endnote|ris|zenodo
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

Example usage, retrieve CITATION.cff from URL with ``curl``, output as BibTeX:

.. code:: bash

    curl https://raw.githubusercontent.com/citation-file-format/cff-converter-python/44a8ad35d94dd50a8b5924d8d26402ae0d162189/CITATION.cff > CITATION.cff
    cffconvert -f bibtex

Results in:

.. code:: bash

    @misc{YourReferenceHere,
    author = {
                Jurriaan H. Spaaks and
                Tom Klaver
             },
    title  = {cff-converter-python},
    month  = {1},
    year   = {2018},
    doi    = {10.5281/zenodo.1162057},
    url    = {https://github.com/citation-file-format/cff-converter-python}
    }

Example usage, let ``cffconvert`` retrieve CITATION.cff from URL, output as ``codemeta.json``:

.. code:: bash

    cffconvert -f codemeta -u https://github.com/citation-file-format/cff-converter-python/tree/master -of codemeta.json

Contents of file ``codemeta.json``:

.. code:: json

    {
        "@context": [
            "https://doi.org/10.5063/schema/codemeta-2.0",
            "http://schema.org"
        ],
        "@type": "SoftwareSourceCode",
        "author": [
            {
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
                "@type": "Person",
                "affiliation": {
                    "@type": "Organization",
                    "legalName": "Netherlands eScience Center"
                },
                "familyName": "Verhoeven",
                "givenName": "Stefan"
            }
        ],
        "codeRepository": "https://github.com/citation-file-format/cff-converter-python",
        "datePublished": "2018-05-22",
        "identifier": "https://doi.org/10.5281/zenodo.1162057",
        "keywords": [
            "citation",
            "bibliography",
            "cff",
            "CITATION.cff"
        ],
        "license": "http://www.apache.org/licenses/LICENSE-2.0",
        "name": "cffconvert",
        "version": "0.0.5"
    }

Convert the contents of a local file ``CITATION.cff`` into the format used by ``.zenodo.json`` files (see
`Zenodo's API docs <http://developers.zenodo.org/#representation>`__), while ignoring any keys that are likely out of date:

.. code:: bash

    cffconvert -f zenodo --ignore-suspect-keys

Results in (note absence of ``date-released``, ``doi``, and ``version``):

.. code:: bash

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


For developers
==============

Install
-------

.. code:: bash

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
    # install any packages used for development such as for testing
    pip install -r requirements-dev.txt
    # install the cffconvert package using symlinks
    pip install --editable .

Running tests
-------------

.. code:: bash

    # (from the project root)

    # run unit tests
    pytest test/

    # run tests against live system (GitHub)
    pytest livetest/


For maintainers
===============

Making a release
----------------

.. code:: bash

    # make sure the release notes are up to date

    # run the live tests and unit tests, make sure they pass

    # git push everything, merge into master as appropriate

    # verify that everything has been pushed and merged by testing as follows
    cd $(mktemp -d)
    git clone https://github.com/citation-file-format/cff-converter-python.git
    cd cff-converter-python
    virtualenv -p /usr/bin/python3.5 myvenv3
    source myvenv3/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    pytest test/
    pytest livetest/

    # register with PyPI test instance https://test.pypi.org

    # remove these directories if you have them
    rm -rf dist
    rm -rf cffconvert-egg.info
    # make a source distribution:
    python setup.py sdist
    # install the 'upload to pypi/testpypi tool' aka twine
    pip install twine
    # upload the contents of the source distribtion we just made
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # checking the package
    # pip install --user --index-url https://test.pypi.org/simple/ cffconvert
    
    # check that the package works as it should when installed from pypitest

    # FINAL STEP: upload to PyPI
    twine upload dist/*

.. |Travis build status| image:: https://travis-ci.org/citation-file-format/cff-converter-python.svg?branch=master
   :target: https://travis-ci.org/citation-file-format/cff-converter-python
.. |Zenodo DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1162057.svg
   :target: https://doi.org/10.5281/zenodo.1162057
.. |PyPi Badge| image:: https://img.shields.io/pypi/v/cffconvert.svg?colorB=blue 
   :target: https://pypi.python.org/pypi/cffconvert/   
.. |Research Software Directory| image:: https://img.shields.io/badge/rsd-cffconvert-00a3e3.svg
   :target: https://www.research-software.nl/software/cff-converter-python
.. |CII Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/1811/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/1811
.. |SonarCloud Quality Gate| image:: https://sonarcloud.io/api/project_badges/measure?project=cff-converter-python&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=cff-converter-python
.. |SonarCloud Code Coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=cff-converter-python&metric=coverage
   :target: https://sonarcloud.io/dashboard?id=cff-converter-python
