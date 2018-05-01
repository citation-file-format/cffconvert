#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version = '1.0.0'

setup(
    name='cffconvert',
    version=__version,
    description='Read CFF formatted CITATION file from a GitHub url and convert it to BibTeX, EndNote, RIS, Codemeta,' +
                ' Zenodo.json, and plain JSON',
    author='Jurriaan H. Spaaks',
    author_email='j.spaaks@esciencecenter.nl',
    license='Apache 2.0',
    url='https://github.com/citation-file-format/cff-converter-python',
    download_url='https://github.com/citation-file-format/cff-converter-python/archive/%s.tar.gz' % __version,
    include_package_data=True,
    keywords=['citation', 'cff', 'CITATION.cff', 'bibliography'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
    ],
    packages=find_packages(),
    install_requires=['PyYAML>=3.12', 'requests>=2.18.4', 'urllib3>=1.22'],
    setup_requires=['pytest', 'pytest-runner'],
    tests_require=['pytest', 'pytest-runner'],
    long_description="""
Read [CFF formatted CITATION](https://github.com/citation-file-format) file from a GitHub
url and convert it to various formats, such as:

1. BibTeX
1. EndNote
1. RIS
1. codemeta
1. plain JSON
1. Zenodo JSON

``cffconvert`` does not support the full
[CFF spec](https://citation-file-format.github.io/assets/pdf/cff-specifications-1.0.3.pdf) yet.



# For users

## Install

```bash
pip install git+https://github.com/citation-file-format/cff-converter-python.git
```

# For developers

## Install

```bash
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
```


## Running tests

```bash
# (from the project root)

# run unit tests
pytest test/

# run tests against live system (GitHub)
pytest livetest/
```
"""
)
