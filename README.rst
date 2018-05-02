|Build Status| |DOI| |Research Software Directory| |CII Best Practices|

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

.. code:: bash

    pip install git+https://github.com/citation-file-format/cff-converter-python.git

Command line interface
----------------------

See ``cffconvert``'s options:

.. code:: bash

    cffconvert --help

Example usage, retrieve CITATION.cff from URL, output as bibtex:

.. code:: bash

    cffconvert https://github.com/citation-file-format/cff-converter-python/tree/master out.txt bibtex

Contents of ``out.txt``:

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

Example usage, retrieve CITATION.cff from URL, output as
``codemeta.json``:

.. code:: bash

    cffconvert https://github.com/citation-file-format/cff-converter-python/tree/master codemeta.json codemeta

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
            }
        ],
        "codeRepository": "https://github.com/citation-file-format/cff-converter-python",
        "datePublished": "2018-01-16",
        "identifier": "https://doi.org/10.5281/zenodo.1162057",
        "keywords": [
            "citation",
            "bibliography",
            "cff",
            "CITATION.cff"
        ],
        "license": "http://www.apache.org/licenses/LICENSE-2.0",
        "name": "cff-converter-python",
        "version": "1.0.0"
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

Running tests
-------------

.. code:: bash

    # (from the project root)

    # run unit tests
    pytest test/

    # run tests against live system (GitHub)
    pytest livetest/

.. |Build Status| image:: https://travis-ci.org/citation-file-format/cff-converter-python.svg?branch=master
   :target: https://travis-ci.org/citation-file-format/cff-converter-python
.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1162057.svg
   :target: https://doi.org/10.5281/zenodo.1162057
.. |Research Software Directory| image:: https://img.shields.io/badge/rsd-cffconvert-00a3e3.svg
   :target: https://www.research-software.nl/software/cff-converter-python
.. |CII Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/1811/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/1811
