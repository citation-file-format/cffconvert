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
