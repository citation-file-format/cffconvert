# 3.0.0 (Unreleased)

## Schema

The schema changes are preliminary and temporary, since they are developed in another repository. I only included them here to keep track of changes.

1. Added `contributors` key, which are currently exactly the same type as `authors`.
2. Added key `relation` to `identifiers`. Its value is an `enum` same as Zenodo's `related_identifiers.relation` (`cites`, `isNewVersionOf`, `isCitedBy`, etc).
3. Updated ISBN regex pattern
4. Updated the schema with new licenses from SPDX license list

## CLI

1. Long outputs, for example those resulting from validation errors, are now truncated by default, but this behavior can be disabled using `--verbose` flag [https://github.com/citation-file-format/cffconvert/issues/278](https://github.com/citation-file-format/cffconvert/issues/278)
1. `cffconvert` exits with non zero code when something went wrong converting or validating [https://github.com/citation-file-format/cffconvert/issues/266](https://github.com/citation-file-format/cffconvert/issues/266)
1. Added "Star on GitHub" footnote in CLI

## Library

1. Added conversion and validation behavior for CFF 1.3
1. Converted metadata now includes information from CFF 1.3 key `contributors` for target formats that support it [https://github.com/citation-file-format/cffconvert/issues/333](https://github.com/citation-file-format/cffconvert/issues/333), [https://github.com/citation-file-format/cffconvert/issues/334](https://github.com/citation-file-format/cffconvert/issues/334)
1. Zenodo metadata now includes `related_identifiers` and optionally `relation_type` such as `citedBy`, `compiles`, `isSupplementTo` etc using CFF 1.3 key `relation` on elements in `identifiers` [https://github.com/citation-file-format/cffconvert/pull/327](https://github.com/citation-file-format/cffconvert/pull/327), [https://github.com/citation-file-format/cffconvert/pull/329](https://github.com/citation-file-format/cffconvert/pull/329)
1. Converted metadata now uses author `email` for target formats that support it [https://github.com/citation-file-format/cffconvert/issues/285](https://github.com/citation-file-format/cffconvert/issues/285)
1. `entity` authors get exported as `Organization` when converting to `schema.org` or `codemeta` (was `Person`) [https://github.com/citation-file-format/cffconvert/issues/239](https://github.com/citation-file-format/cffconvert/issues/239)
1. CFF key `name` takes precedence over `alias` when converting entity authors (was the other way around) [https://github.com/citation-file-format/cffconvert/issues/308](https://github.com/citation-file-format/cffconvert/issues/308)
1. `schema.org` and `codemeta` conversion export an affiliation name as `name` (was `legalName`) [https://github.com/citation-file-format/cffconvert/issues/272](https://github.com/citation-file-format/cffconvert/issues/272)
1. Added `"upload_type": "software"` when exporting to Zenodo from CFF files that use schema versions 1.0.x or 1.1.x [https://github.com/citation-file-format/cffconvert/issues/306](https://github.com/citation-file-format/cffconvert/issues/306)
1. Apalike conversion now uses "and" or ", and" to concatenate author names when there are 2 or more authors [https://github.com/citation-file-format/cffconvert/issues/226](https://github.com/citation-file-format/cffconvert/issues/226)
1. Bibtex conversion now uses braces to protect names of entity authors [https://github.com/citation-file-format/cffconvert/issues/156](https://github.com/citation-file-format/cffconvert/issues/156)
1. Library now explicitly exports Citation and nothing else
1. Requests to GitHub now use versioned API 
1. Requests to GitHub can now be authenticated via environment variable CFFCONVERT_API_TOKEN for higher rate limit [https://github.com/citation-file-format/cffconvert/issues/353](https://github.com/citation-file-format/cffconvert/issues/353)
1. Requests to GitHub now use the target repo's default branch if user leaves branch unspecified [https://github.com/citation-file-format/cffconvert/issues/263](https://github.com/citation-file-format/cffconvert/issues/263)

## Development

1. Changed the repo name from `cff-converter-python` to just `cffconvert` [https://github.com/citation-file-format/cffconvert/issues/283](https://github.com/citation-file-format/cffconvert/issues/283)
1. Moved to a `src/` directory layout [https://github.com/citation-file-format/cffconvert/issues/311](https://github.com/citation-file-format/cffconvert/issues/311)
1. Clearer separation between `cli` parts and `lib` parts [https://github.com/citation-file-format/cffconvert/issues/276](https://github.com/citation-file-format/cffconvert/issues/276)
1. Replaced `setup.cfg` and `setup.py` with `pyproject.toml` [https://github.com/citation-file-format/cffconvert/issues/312](https://github.com/citation-file-format/cffconvert/issues/312)
1. Added `pytest` markers for `apalike`, `bibtex`, `codemeta`, `endnote`, `ris`, `schemaorg`, `zenodo` tests [https://github.com/citation-file-format/cffconvert/pull/330](https://github.com/citation-file-format/cffconvert/pull/330)
1. Added `pytest` marker `lib` for library tests and `cli` for command line interface tests
1. Refactored testing directory layout/naming to facilitate testing subparts of the test tree [https://github.com/citation-file-format/cffconvert/pull/315](https://github.com/citation-file-format/cffconvert/pull/315)
1. Consistent styling now enforced with ruff [https://github.com/citation-file-format/cffconvert/pull/339](https://github.com/citation-file-format/cffconvert/pull/339)
1. Added linting via `pre-commit` (`isort`, `pyroma`, `ruff`, `prospector`) [https://github.com/citation-file-format/cffconvert/pull/324](https://github.com/citation-file-format/cffconvert/pull/324)
1. Added Markdown link checker pre-commit hook
1. Added `cffconvert` metadata validation checker via `pre-commit`
1. Updated `jsonschema` dependency to a wider range, now includes 4.x [https://github.com/citation-file-format/cffconvert/issues/292](https://github.com/citation-file-format/cffconvert/issues/292)
1. Updated python versions used in CI [https://github.com/citation-file-format/cffconvert/pull/295](https://github.com/citation-file-format/cffconvert/pull/295)
1. Added tests to verify that behavior maps such as those for authors or URLs implement all possible keys, that there are no extra keys, and that there are no extra methods. [https://github.com/citation-file-format/cffconvert/issues/300](https://github.com/citation-file-format/cffconvert/issues/300)
1. Added missing `codemeta` tests to `1.2.0/author-creators` [https://github.com/citation-file-format/cffconvert/pull/355](https://github.com/citation-file-format/cffconvert/pull/355)
1. Fixed bug with YAML parsing related to testing order [https://github.com/citation-file-format/cffconvert/issues/343](https://github.com/citation-file-format/cffconvert/issues/343)
1. Fixed invalid CFF in one of the tests [https://github.com/citation-file-format/cffconvert/issues/297](https://github.com/citation-file-format/cffconvert/issues/297)

## Other 

1. `cffconvert` is now available as a `pre-commit` hook with id `validate-cff` [https://github.com/citation-file-format/cffconvert/pull/269](https://github.com/citation-file-format/cffconvert/pull/269)
1. Updated the Dockerfile to use latest version of cffconvert and recent version of Alpine [https://github.com/citation-file-format/cffconvert/pull/340](https://github.com/citation-file-format/cffconvert/pull/340)

# 2.0.0

## CLI

- added APA output (PR [#149](https://github.com/citation-file-format/cffconvert/pull/149); thanks [@wleoncio](https://github.com/wleoncio))
- added support for validation and conversion of `CITATION.cff` files with `cff-version: 1.2.0`
- argument `--outputformat` was renamed to `--format`
- argument `-ig`, `--ignore-suspect-keys` was removed
- argument `--verbose` was removed
- argument `--show-trace` was added
 
## Library

- added APA output (PR [#149](https://github.com/citation-file-format/cffconvert/pull/149); thanks [@wleoncio](https://github.com/wleoncio))
- added support for validation and conversion of `CITATION.cff` files with `cff-version: 1.2.0`
- simplified the `Citation` class and its interface
- `cli` is no longer part of the public interface of the library
- URLs are now constructed from `identifiers`, `repository`, `repository-artifact`, `repository-code`, or `url`, with a transparent mechanism to choose what to use given the data that is available from a given `CITATION.cff` file
- Authors are now constructed from `given-names`, `family-names` (including `name-particle` and `name-suffix`), `alias`, `name`, `affiliation` and `orcid`, with a transparent mechanism to choose what to use given the data that is available from a given `CITATION.cff` file

## Other

- switched to static configuration (setup.cfg over setup.py)
- dependencies are now in `setup.cfg` as opposed to `requirements[-dev].txt`
- updated version ranges for dependencies
- tests are no longer `unittest.TestCase` based, but pytest with fixtures
- added jsonschema based validation for CITATION.cff files with `cff-version: 1.2.0`
- implemented _State pattern_ for `Citation` to help it deal with multiple behaviors under past and future versions of the Citation File Format.
- switched from TravisCI to GitHub Actions workflows, added linting and publishing workflows
- CI is now testing against Python 3.6, 3.7, 3.8, and 3.9 on Mac, Linux and Windows
- copies of the relevant schemas are now bundled with the package 
- organized the tests to be more orthogonal to each other / less overlap between tests

# 1.3.3

-   With recent changes to the release process, the schema will be in a
    different place than before. This release fixes
    <https://github.com/citation-file-format/cffconvert/issues/119>).

# 1.3.2

-   the ruamel.yaml dependency was not specified tightly enough,
    `requirements.txt` has been updated as have the notes for
    maintainers.

# 1.3.1

-   'cff-version: 1.0.3' is now interpreted as 1.0.3-1 (the latest
    schema version that implements the spec 1.0.3). This will fix some
    problems with the list of SPDX license abbreviations. These
    additional licenses should now work:
    -   `AGPL-3.0-only`
    -   `AGPL-3.0-or-later`
    -   `BSD-1-Clause`
    -   `BSD-2-Clause-Patent`
    -   `CDLA-Permissive-1.0`
    -   `CDLA-Sharing-1.0`
    -   `EPL-2.0`
    -   `EUPL-1.2`
    -   `GFDL-1.1-only`
    -   `GFDL-1.1-or-later`
    -   `GFDL-1.2-only`
    -   `GFDL-1.2-or-later`
    -   `GFDL-1.3-only`
    -   `GFDL-1.3-or-later`
    -   `GPL-1.0-only`
    -   `GPL-1.0-or-later`
    -   `GPL-2.0-only`
    -   `GPL-2.0-or-later`
    -   `GPL-3.0-only`
    -   `GPL-3.0-or-later`
    -   `LGPL-2.0-only`
    -   `LGPL-2.0-or-later`
    -   `LGPL-2.1-only`
    -   `LGPL-2.1-or-later`
    -   `LGPL-3.0-only`
    -   `LGPL-3.0-or-later`

# 1.3.0

-   added schema.org converter method

# 1.2.2

-   added documentation for the Google Cloud Function interface

# 1.2.1

-   setup.py no longer includes test dependencies as install
    dependencies

# 1.2.0

-   corrected an error where cffconvert could not raise an error during
    validation
    (<https://github.com/citation-file-format/cffconvert/issues/94>).

# 1.1.0

-   replaced pykwalifire with its parent pykwalify
-   now works for python 3.7 (refs \#80)
-   not using PyYAML anymore (but it still comes along with pykwalify
    for some reason)
-   added a function that can be used as Google Cloud function
-   hopefully fixed parsing of strings that should have been entered as
    dates (the new validator does not find that offensive, hence I had
    to fix it myself)

# 1.0.4

-   replaced PyYAML dependency with ruamel.yaml

# 1.0.3

-   security bugfix by updating requests from 2.18.4 to 2.20.0

# 1.0.2

-   fixed bug
    <https://github.com/citation-file-format/cffconvert/issues/82>
    (warnings on stdout)

# 1.0.1

-   fixed bug
    <https://github.com/citation-file-format/cffconvert/issues/73>
    (orcid format in zenodo export)

# 1.0.0

-   first stable release
-   solved bug
    <https://github.com/citation-file-format/cffconvert/issues/59>
    (cffconvert creates local file `data.yaml` and `schema.yaml` on
    validate)

# 0.0.5

-   Minor changes

# 0.0.4

-   added optional validation of CITATION.cff files using pykwalifire
    (`--validate`)
-   added printing the CITATION.cff contents from the command line
-   added unit tests for command line interface
-   added integration with sonarcloud code quality monitoring
-   removed shorthand command line argument `-v` (represented both
    `--validate` and --verbose)
-   added showing its own version (`--version`)
-   command line argument `--ignore-suspect-keys` no longer needs to be
    assigned a value, it's simply a flag

