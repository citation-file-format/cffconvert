1.3.1
=====

- 'cff-version: 1.0.3' is now interpreted as 1.0.3-1 (the latest schema version that implements the spec 1.0.3). This will fix some problems with the list of SPDX license abbreviations. These additional licenses should now work:
    
  - ``AGPL-3.0-only``
  - ``AGPL-3.0-or-later``
  - ``BSD-1-Clause``
  - ``BSD-2-Clause-Patent``
  - ``CDLA-Permissive-1.0``
  - ``CDLA-Sharing-1.0``
  - ``EPL-2.0``
  - ``EUPL-1.2``
  - ``GFDL-1.1-only``
  - ``GFDL-1.1-or-later``
  - ``GFDL-1.2-only``
  - ``GFDL-1.2-or-later``
  - ``GFDL-1.3-only``
  - ``GFDL-1.3-or-later``
  - ``GPL-1.0-only``
  - ``GPL-1.0-or-later``
  - ``GPL-2.0-only``
  - ``GPL-2.0-or-later``
  - ``GPL-3.0-only``
  - ``GPL-3.0-or-later``
  - ``LGPL-2.0-only``
  - ``LGPL-2.0-or-later``
  - ``LGPL-2.1-only``
  - ``LGPL-2.1-or-later``
  - ``LGPL-3.0-only``
  - ``LGPL-3.0-or-later``

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
