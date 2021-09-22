# Documentation for developers

## Install


```shell
# get a copy of the cff-converter-python software
git clone https://github.com/citation-file-format/cff-converter-python.git
# change directory into cff-converter-python
cd cff-converter-python
# make a virtual environment named env
python3 -m venv env
# activate the virtual environment
source env/bin/activate
# upgrade pip, wheel, setuptools
pip install --upgrade pip wheel setuptools
# install cffconvert itself
pip install --editable .
# install any packages used for development such as for testing
pip install --editable .[dev]
```

## Running tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# (from the project root)

# run unit tests
python3 -m pytest test/1.2.0
python3 -m pytest test/1.1.0
python3 -m pytest test/1.0.3

# tests for consistent file naming
bash test/test_consistent_file_naming.sh dir=test/
bash test/test_consistent_file_naming.sh dir=livetest/

# tests for consistent versioning
python3 -m pytest test/test_consistent_versioning.py
```

## Running linters locally

For linting we use [prospector](https://pypi.org/project/prospector/) and to sort imports we will use
[isort](https://pycqa.github.io/isort/). Running the linters requires an activated virtual environment with the
development tools installed.

```shell
# linter
prospector

# recursively check import style for the cffconvert module only
isort --recursive --check-only cffconvert

# recursively check import style for the cffconvert module only and show
# any proposed changes as a diff
isort --recursive --check-only --diff cffconvert

# recursively fix import style for the cffconvert module only
isort --recursive cffconvert
```

To fix readability of your code style you can use [yapf](https://github.com/google/yapf).

Developers should consider enabling automatic linting with `prospector` and `isort` on commit by enabling the git hook from `.githooks/pre-commit`, like so:

```shell
git config --local core.hooksPath .githooks
```


## For maintainers

### Making a release


1. make sure the release notes are up to date
1. run the live tests and unit tests, make sure they pass
1. 

    ```shell
    # remove old cffconvert from your system if you have it
    python3 -m pip uninstall cffconvert

    # this next command should now return empty
    which cffconvert

    # install the package to user space, using no caching (can bring to light dependency problems)
    python3 -m pip install --user --no-cache-dir --editable .
    # check if cffconvert works, e.g.
    cffconvert --version

    # git push everything, merge into main as appropriate

    # verify that everything has been pushed and merged by testing as follows
    cd $(mktemp -d --tmpdir cffconvert-release.XXXXXX)
    git clone https://github.com/citation-file-format/cff-converter-python.git .
    python3 -m venv env
    source env/bin/activate
    pip install --no-cache-dir .[dev]

    # run the tests according to section above

    # register with PyPI test instance https://test.pypi.org

    # remove these directories if you have them
    rm -rf dist
    rm -rf cffconvert-egg.info
    # make a source distribution:
    python setup.py sdist
    # install the 'upload to pypi/testpypi tool' aka twine
    pip install .[publishing]
    # upload the contents of the source distribution we just made
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # checking the package
    python3 -m pip -v install --user --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple cffconvert

    # check that the package works as it should when installed from pypitest

    # FINAL STEP: upload to PyPI
    twine upload dist/*
    ```

### Building the docker image

```shell
# (requires 2.0.0 to be downloadable from PyPI)
docker build --tag cffconvert:2.0.0 .
docker build --tag cffconvert:latest .
```

### Publishing on DockerHub

See <https://docs.docker.com/docker-hub/repos/#pushing-a-docker-container-image-to-docker-hub> for more information on publishing.

```shell
# re-tag existing image
docker tag cffconvert:2.0.0 citationcff/cffconvert:2.0.0

# publish
docker push citationcff/cffconvert:2.0.0
```
