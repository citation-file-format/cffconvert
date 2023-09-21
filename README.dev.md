# Documentation for developers

## Installing

```shell
# get a copy of the cffconvert software
git clone https://github.com/citation-file-format/cffconvert.git

# change directory into cffconvert
cd cffconvert

# make a virtual environment named venv
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# upgrade pip, wheel, setuptools
pip install --upgrade pip wheel setuptools

# install cffconvert  in editable mode
pip install --editable .
```

There are various sets of dependencies that you should install depending on the work you're planning to do.

```shell
pip install --editable .[dev]
```

```shell
pip install --editable .[gcloud]
```

```shell
pip install --editable .[publishing]
```

```shell
pip install --editable .[testing]
```

You can combine these into one command like so, e.g.:

```shell
pip install --editable .[dev,testing]
```

## Testing

```shell
# (from the project root)
pip install --editable .[testing]

# run all tests
pytest tests/

# run tests for consistent versioning
pytest tests/test_consistent_versioning.py

# run pytest on a subset of the files, e.g.
cd tests/lib/cff_1_2_0/ && pytest .
```

Tests pertaining to a specific exporter have been marked accordingly with one of the following markers (see also
`pytest` configuration section in `pyproject.toml`):

1. `apalike`
2. `bibtex`
3. `codemeta`
4. `endnote`
5. `ris`
6. `schemaorg`
7. `zenodo`

Additionally, there are markers for CLI tests and for library tests:

1. `cli`
2. `lib`

You can instruct `pytest` to run only the tests for one or some of these marked sets. As an example, if you want to run
only the tests related to exporting as Endnote, you should call `pytest` with the `-m` flag as follows:

```shell
pytest -m endnote
```

Markers can also be combined with `or` and `and` and `not`, e.g.

```shell
pytest -m 'endnote and lib'
pytest -m 'cli and not zenodo'
pytest -m 'schemaorg or codemeta'
# etc
```

## Linting

Running the linters requires that the development tools have been installed:

```shell
pip install --editable .[dev]
```

Sorting Python import lines with '`isort`' (https://pycqa.github.io/isort/):

```shell
# recursively check import style for the cffconvert module only
isort --check-only src/cffconvert

# recursively check import style for the cffconvert module only and show
# any proposed changes as a diff
isort --check-only --diff src/cffconvert

# recursively fix import style for the cffconvert module only
isort src/cffconvert
```

Linting the code base by running a variety of other tools via '`prospector`' (https://github.com/landscapeio/prospector):

```shell
# linter
prospector
```

Assessing the package metadata using '`pyroma`' (https://github.com/regebro/pyroma):

```shell
# from the project root
pyroma .
```

Linting the code base using '`ruff`' (https://github.com/astral-sh/ruff):

```shell
ruff check path/to/code/
```

The linting tools are also usable via [`pre-commit`](https://pre-commit.com/):

```shell
# Run all tools
pre-commit run --all-files

# Run a specific tool, see .pre-commit-config.yaml for their IDs
pre-commit run --all-files <ID of the task>
```

Alternatively, the linting tools can be set up to run automatically whenever you issue a `git commit` command, as
follows:
 
```shell
pre-commit install
```

## Construction of author keys

There are various source keys in CFF that can be used to convert to a target format. The code uses a pattern of first
identifiying what information is present, then summarizing this as a key, then using that key to retrieve a method which 
is tailored only to that specific combination of source keys. As an example of this mapping, see the setup in
https://github.com/citation-file-format/cffconvert/blob/3.0.0a0/cffconvert/behavior_shared/schemaorg_author_shared.py

Source keys:

1. `authors[i].given-names`
2. `authors[i].family-names` (including name particle and suffix)
3. `authors[i].alias`
4. `authors[i].name`
5. `authors[i].affiliation`
6. `authors[i].orcid`
7. `authors[i].email`

The table below lists how the key name is constructed based what information was provided in the `CITATION.cff` file:

| key          | has given name | has family name | has alias | has name | has affiliation | has orcid | has email |
|--------------|----------------|-----------------|-----------|----------|-----------------|-----------|-----------|
| `GFANAOE`    | True           | True            | True      | True     | True            | True      | True      |
| `GFANA_E`    | True           | True            | True      | True     | True            | False     | True      |
| `GFAN_OE`    | True           | True            | True      | True     | False           | True      | True      |
| `GFAN__E`    | True           | True            | True      | True     | False           | False     | True      |
| `GFA_AOE`    | True           | True            | True      | False    | True            | True      | True      |
| `GFA_A_E`    | True           | True            | True      | False    | True            | False     | True      |
| `GFA__OE`    | True           | True            | True      | False    | False           | True      | True      |
| `GFA___E`    | True           | True            | True      | False    | False           | False     | True      |
| `GF_NAOE`    | True           | True            | False     | True     | True            | True      | True      |
| `GF_NA_E`    | True           | True            | False     | True     | True            | False     | True      |
| `GF_N_OE`    | True           | True            | False     | True     | False           | True      | True      |
| `GF_N__E`    | True           | True            | False     | True     | False           | False     | True      |
| `GF__AOE`    | True           | True            | False     | False    | True            | True      | True      |
| `GF__A_E`    | True           | True            | False     | False    | True            | False     | True      |
| `GF___OE`    | True           | True            | False     | False    | False           | True      | True      |
| `GF____E`    | True           | True            | False     | False    | False           | False     | True      |
| `G_ANAOE`    | True           | False           | True      | True     | True            | True      | True      |
| `G_ANA_E`    | True           | False           | True      | True     | True            | False     | True      |
| `G_AN_OE`    | True           | False           | True      | True     | False           | True      | True      |
| `G_AN__E`    | True           | False           | True      | True     | False           | False     | True      |
| `G_A_AOE`    | True           | False           | True      | False    | True            | True      | True      |
| `G_A_A_E`    | True           | False           | True      | False    | True            | False     | True      |
| `G_A__OE`    | True           | False           | True      | False    | False           | True      | True      |
| `G_A___E`    | True           | False           | True      | False    | False           | False     | True      |
| `G__NAOE`    | True           | False           | False     | True     | True            | True      | True      |
| `G__NA_E`    | True           | False           | False     | True     | True            | False     | True      |
| `G__N_OE`    | True           | False           | False     | True     | False           | True      | True      |
| `G__N__E`    | True           | False           | False     | True     | False           | False     | True      |
| `G___AOE`    | True           | False           | False     | False    | True            | True      | True      |
| `G___A_E`    | True           | False           | False     | False    | True            | False     | True      |
| `G____OE`    | True           | False           | False     | False    | False           | True      | True      |
| `G_____E`    | True           | False           | False     | False    | False           | False     | True      |
| `_FANAOE`    | False          | True            | True      | True     | True            | True      | True      |
| `_FANA_E`    | False          | True            | True      | True     | True            | False     | True      |
| `_FAN_OE`    | False          | True            | True      | True     | False           | True      | True      |
| `_FAN__E`    | False          | True            | True      | True     | False           | False     | True      |
| `_FA_AOE`    | False          | True            | True      | False    | True            | True      | True      |
| `_FA_A_E`    | False          | True            | True      | False    | True            | False     | True      |
| `_FA__OE`    | False          | True            | True      | False    | False           | True      | True      |
| `_FA___E`    | False          | True            | True      | False    | False           | False     | True      |
| `_F_NAOE`    | False          | True            | False     | True     | True            | True      | True      |
| `_F_NA_E`    | False          | True            | False     | True     | True            | False     | True      |
| `_F_N_OE`    | False          | True            | False     | True     | False           | True      | True      |
| `_F_N__E`    | False          | True            | False     | True     | False           | False     | True      |
| `_F__AOE`    | False          | True            | False     | False    | True            | True      | True      |
| `_F__A_E`    | False          | True            | False     | False    | True            | False     | True      |
| `_F___OE`    | False          | True            | False     | False    | False           | True      | True      |
| `_F____E`    | False          | True            | False     | False    | False           | False     | True      |
| `__ANAOE`    | False          | False           | True      | True     | True            | True      | True      |
| `__ANA_E`    | False          | False           | True      | True     | True            | False     | True      |
| `__AN_OE`    | False          | False           | True      | True     | False           | True      | True      |
| `__AN__E`    | False          | False           | True      | True     | False           | False     | True      |
| `__A_AOE`    | False          | False           | True      | False    | True            | True      | True      |
| `__A_A_E`    | False          | False           | True      | False    | True            | False     | True      |
| `__A__OE`    | False          | False           | True      | False    | False           | True      | True      |
| `__A___E`    | False          | False           | True      | False    | False           | False     | True      |
| `___NAOE`    | False          | False           | False     | True     | True            | True      | True      |
| `___NA_E`    | False          | False           | False     | True     | True            | False     | True      |
| `___N_OE`    | False          | False           | False     | True     | False           | True      | True      |
| `___N__E`    | False          | False           | False     | True     | False           | False     | True      |
| `____AOE`    | False          | False           | False     | False    | True            | True      | True      |
| `____A_E`    | False          | False           | False     | False    | True            | False     | True      |
| `_____OE`    | False          | False           | False     | False    | False           | True      | True      |
| `______E`    | False          | False           | False     | False    | False           | False     | True      |
| `GFANAO_`    | True           | True            | True      | True     | True            | True      | False     |
| `GFANA__`    | True           | True            | True      | True     | True            | False     | False     |
| `GFAN_O_`    | True           | True            | True      | True     | False           | True      | False     |
| `GFAN___`    | True           | True            | True      | True     | False           | False     | False     |
| `GFA_AO_`    | True           | True            | True      | False    | True            | True      | False     |
| `GFA_A__`    | True           | True            | True      | False    | True            | False     | False     |
| `GFA__O_`    | True           | True            | True      | False    | False           | True      | False     |
| `GFA____`    | True           | True            | True      | False    | False           | False     | False     |
| `GF_NAO_`    | True           | True            | False     | True     | True            | True      | False     |
| `GF_NA__`    | True           | True            | False     | True     | True            | False     | False     |
| `GF_N_O_`    | True           | True            | False     | True     | False           | True      | False     |
| `GF_N___`    | True           | True            | False     | True     | False           | False     | False     |
| `GF__AO_`    | True           | True            | False     | False    | True            | True      | False     |
| `GF__A__`    | True           | True            | False     | False    | True            | False     | False     |
| `GF___O_`    | True           | True            | False     | False    | False           | True      | False     |
| `GF_____`    | True           | True            | False     | False    | False           | False     | False     |
| `G_ANAO_`    | True           | False           | True      | True     | True            | True      | False     |
| `G_ANA__`    | True           | False           | True      | True     | True            | False     | False     |
| `G_AN_O_`    | True           | False           | True      | True     | False           | True      | False     |
| `G_AN___`    | True           | False           | True      | True     | False           | False     | False     |
| `G_A_AO_`    | True           | False           | True      | False    | True            | True      | False     |
| `G_A_A__`    | True           | False           | True      | False    | True            | False     | False     |
| `G_A__O_`    | True           | False           | True      | False    | False           | True      | False     |
| `G_A____`    | True           | False           | True      | False    | False           | False     | False     |
| `G__NAO_`    | True           | False           | False     | True     | True            | True      | False     |
| `G__NA__`    | True           | False           | False     | True     | True            | False     | False     |
| `G__N_O_`    | True           | False           | False     | True     | False           | True      | False     |
| `G__N___`    | True           | False           | False     | True     | False           | False     | False     |
| `G___AO_`    | True           | False           | False     | False    | True            | True      | False     |
| `G___A__`    | True           | False           | False     | False    | True            | False     | False     |
| `G____O_`    | True           | False           | False     | False    | False           | True      | False     |
| `G______`    | True           | False           | False     | False    | False           | False     | False     |
| `_FANAO_`    | False          | True            | True      | True     | True            | True      | False     |
| `_FANA__`    | False          | True            | True      | True     | True            | False     | False     |
| `_FAN_O_`    | False          | True            | True      | True     | False           | True      | False     |
| `_FAN___`    | False          | True            | True      | True     | False           | False     | False     |
| `_FA_AO_`    | False          | True            | True      | False    | True            | True      | False     |
| `_FA_A__`    | False          | True            | True      | False    | True            | False     | False     |
| `_FA__O_`    | False          | True            | True      | False    | False           | True      | False     |
| `_FA____`    | False          | True            | True      | False    | False           | False     | False     |
| `_F_NAO_`    | False          | True            | False     | True     | True            | True      | False     |
| `_F_NA__`    | False          | True            | False     | True     | True            | False     | False     |
| `_F_N_O_`    | False          | True            | False     | True     | False           | True      | False     |
| `_F_N___`    | False          | True            | False     | True     | False           | False     | False     |
| `_F__AO_`    | False          | True            | False     | False    | True            | True      | False     |
| `_F__A__`    | False          | True            | False     | False    | True            | False     | False     |
| `_F___O_`    | False          | True            | False     | False    | False           | True      | False     |
| `_F_____`    | False          | True            | False     | False    | False           | False     | False     |
| `__ANAO_`    | False          | False           | True      | True     | True            | True      | False     |
| `__ANA__`    | False          | False           | True      | True     | True            | False     | False     |
| `__AN_O_`    | False          | False           | True      | True     | False           | True      | False     |
| `__AN___`    | False          | False           | True      | True     | False           | False     | False     |
| `__A_AO_`    | False          | False           | True      | False    | True            | True      | False     |
| `__A_A__`    | False          | False           | True      | False    | True            | False     | False     |
| `__A__O_`    | False          | False           | True      | False    | False           | True      | False     |
| `__A____`    | False          | False           | True      | False    | False           | False     | False     |
| `___NAO_`    | False          | False           | False     | True     | True            | True      | False     |
| `___NA__`    | False          | False           | False     | True     | True            | False     | False     |
| `___N_O_`    | False          | False           | False     | True     | False           | True      | False     |
| `___N___`    | False          | False           | False     | True     | False           | False     | False     |
| `____AO_`    | False          | False           | False     | False    | True            | True      | False     |
| `____A__`    | False          | False           | False     | False    | True            | False     | False     |
| `_____O_`    | False          | False           | False     | False    | False           | True      | False     |
| `_______`    | False          | False           | False     | False    | False           | False     | False     |

## Construction of identifier keys

There are various source keys in CFF that can be used to convert to a target format. The code uses a pattern of first
identifiying what information is present, then summarizing this as a key, then using that key to retrieve a method which 
is tailored only to that specific combination of source keys. 

Source keys: 

- `doi`
- `identifiers[i].type==doi`

The table below lists how the key name is constructed based what information was provided in the `CITATION.cff` file:

| key  | has doi | has identifiers doi |
|------|---------|---------------------|
| `__` | False   | False               |
| `_I` | False   | True                |
| `D_` | True    | False               |
| `DI` | True    | True                |

## Construction of URL keys

There are various source keys in CFF that can be used to convert to a target format. The code uses a pattern of first
identifiying what information is present, then summarizing this as a key, then using that key to retrieve a method which 
is tailored only to that specific combination of source keys. 

Source keys:

- `identifiers[i].type==url`
- `repository`
- `repository-artifact`
- `repository-code`
- `url`

The table below lists how the key name is constructed based what information was provided in the `CITATION.cff` file:

| key     | has indentifiers url | has repository | has repository-artifact | has repository-code | has url |
|---------|----------------------|----------------|-------------------------|---------------------|---------|
| `IRACU` | True                 | True           | True                    | True                | True    |
| `IRAC_` | True                 | True           | True                    | True                | False   |
| `IRA_U` | True                 | True           | True                    | False               | True    |
| `IRA__` | True                 | True           | True                    | False               | False   |
| `IR_CU` | True                 | True           | False                   | True                | True    |
| `IR_C_` | True                 | True           | False                   | True                | False   |
| `IR__U` | True                 | True           | False                   | False               | True    |
| `IR___` | True                 | True           | False                   | False               | False   |
| `I_ACU` | True                 | False          | True                    | True                | True    |
| `I_AC_` | True                 | False          | True                    | True                | False   |
| `I_A_U` | True                 | False          | True                    | False               | True    |
| `I_A__` | True                 | False          | True                    | False               | False   |
| `I__CU` | True                 | False          | False                   | True                | True    |
| `I__C_` | True                 | False          | False                   | True                | False   |
| `I___U` | True                 | False          | False                   | False               | True    |
| `I____` | True                 | False          | False                   | False               | False   |
| `_RACU` | False                | True           | True                    | True                | True    |
| `_RAC_` | False                | True           | True                    | True                | False   |
| `_RA_U` | False                | True           | True                    | False               | True    |
| `_RA__` | False                | True           | True                    | False               | False   |
| `_R_CU` | False                | True           | False                   | True                | True    |
| `_R_C_` | False                | True           | False                   | True                | False   |
| `_R__U` | False                | True           | False                   | False               | True    |
| `_R___` | False                | True           | False                   | False               | False   |
| `__ACU` | False                | False          | True                    | True                | True    |
| `__AC_` | False                | False          | True                    | True                | False   |
| `__A_U` | False                | False          | True                    | False               | True    |
| `__A__` | False                | False          | True                    | False               | False   |
| `___CU` | False                | False          | False                   | True                | True    |
| `___C_` | False                | False          | False                   | True                | False   |
| `____U` | False                | False          | False                   | False               | True    |
| `_____` | False                | False          | False                   | False               | False   |

## For maintainers

### Making a release


1. make sure the release notes are up to date
2. preparation

    ```shell
    # remove old cffconvert from your system if you have it
    python3 -m pip uninstall cffconvert

    # this next command should now return empty
    which cffconvert

    # install the package to user space, using no caching (can bring to light dependency problems)
    python3 -m pip install --user --no-cache-dir .

    # check if cffconvert works, e.g.
    cffconvert --version
    
    # run the tests, make sure they pass
    python3 -m pip pytest tests

    # git push everything, merge into main as appropriate
    ```
    
3. publishing on test instance of PyPI

    ```shell
    # verify that everything has been pushed and merged by testing as follows
    cd $(mktemp -d --tmpdir cffconvert-release.XXXXXX)
    git clone https://github.com/citation-file-format/cffconvert.git .
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip wheel setuptools
    python3 -m pip install --no-cache-dir .

    # register with PyPI test instance https://test.pypi.org

    # remove these directories if you have them
    rm -rf dist
    rm -rf cffconvert-egg.info
    # make a source distribution:
    python setup.py sdist
    # make a wheel
    python setup.py bdist_wheel 
    # install the 'upload to pypi/testpypi tool' aka twine
    pip install .[publishing]
    # upload the contents of the source distribution we just made (requires credentials for test.pypi.org)
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```
    
4. Checking the package

    Open another shell but keep the other one. We'll return to the first shell momentarily.
    
    Verify that there is a new version of the package on Test PyPI https://test.pypi.org/project/cffconvert/

    ```shell
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple cffconvert

    # check that the package works as it should when installed from pypitest
    ```
5. FINAL STEP: upload to PyPI

    Go back to the first shell, then (requires credentials for pypi.org)

    ```shell
    twine upload dist/*
    ```
6. Make the release on GitHub
7. Go to Zenodo, log in to inspect the draft. Then click `Publish` to finalize it.

### Building the docker image

```shell
# (requires 3.0.0a0 to be downloadable from PyPI)
docker build --tag cffconvert:3.0.0a0 .
docker build --tag cffconvert:latest .
```

See if the Docker image works as expected:
```shell
docker run --rm -v $PWD:/app cffconvert --validate
docker run --rm -v $PWD:/app cffconvert --version
docker run --rm -v $PWD:/app cffconvert
# etc
```

### Publishing on DockerHub

See <https://docs.docker.com/docker-hub/repos/#pushing-a-docker-container-image-to-docker-hub> for more information on publishing.

```shell
# log out of any dockerhub credentials
docker logout

# log back in with username 'citationcff' credentials
docker login

# re-tag existing images
docker tag cffconvert:3.0.0a0 citationcff/cffconvert:3.0.0a0
docker tag cffconvert:latest citationcff/cffconvert:latest

# publish
docker push citationcff/cffconvert:3.0.0a0
docker push citationcff/cffconvert:latest
```
