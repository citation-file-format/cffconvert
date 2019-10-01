1.3.0
=====

- added schema.org converter method

1.2.2
=====

- added documentation for the Google Cloud Function interface

1.2.1
=====

- setup.py no longer includes test dependencies as install dependencies

1.2.0
=====

- corrected an error where cffconvert could not raise an error during validation (https://github.com/citation-file-format/cff-converter-python/issues/94).

1.1.0
=====

- replaced pykwalifire with its parent pykwalify
- now works for python 3.7 (refs #80)
- not using PyYAML anymore (but it still comes along with pykwalify for some reason)
- added a function that can be used as Google Cloud function
- hopefully fixed parsing of strings that should have been entered as dates (the new validator does
  not find that offensive, hence I had to fix it myself)

1.0.4
=====

- replaced PyYAML dependency with ruamel.yaml

1.0.3
=====

- security bugfix by updating requests from 2.18.4 to 2.20.0

1.0.2
=====

- fixed bug https://github.com/citation-file-format/cff-converter-python/issues/82 (warnings on stdout)

1.0.1
=====

- fixed bug https://github.com/citation-file-format/cff-converter-python/issues/73 (orcid format in zenodo export)

1.0.0
=====

- first stable release
- solved bug
  https://github.com/citation-file-format/cff-converter-python/issues/59
  (cffconvert creates local file ``data.yaml`` and ``schema.yaml`` on validate)

0.0.5
=====

- Minor changes

0.0.4
=====

- added optional validation of CITATION.cff files using pykwalifire (``--validate``)
- added printing the CITATION.cff contents from the command line
- added unit tests for command line interface
- added integration with sonarcloud code quality monitoring
- removed shorthand command line argument ``-v`` (represented both ``--validate`` and --verbose)
- added showing its own version (``--version``)
- command line argument ``--ignore-suspect-keys`` no longer needs to be assigned a value, it's simply a flag
