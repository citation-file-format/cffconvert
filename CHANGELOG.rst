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
