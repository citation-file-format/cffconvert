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
      -if, --infile TEXT              Path to the CITATION.cff input file.
      -of, --outfile TEXT             Path to the output file.
      -f, --outputformat TEXT         Output format: bibtex|codemeta|endnote|ris|zenodo  [required]
      -u, --url TEXT                  URL of the repo containing the CITATION.cff (currently only github.com is supported;
                                      may include branch name, commit sha, tag name). For example:
                                      'https://github.com/citation-file-format/cff-converter-python' or
                                      'https://github.com/citation-file-format/cff-converter-python/tree/master'
      -v, --validate                  Validate the CITATION.cff found at the URL or supplied through '--infile'
      -ig, --ignore-suspect-keys BOOLEAN
                                      If True, ignore any keys from CITATION.cff that are likely out of date, such as
                                      'commit', 'date-released', 'doi', and 'version'.
      -v, --verbose                   Provide feedback on what was entered.
      --help                          Show this message and exit.


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
        "title": "cff-converter-python"
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
