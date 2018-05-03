#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version = '0.0.3'

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    name='cffconvert',
    py_modules=["cffconvert"],
    entry_points="""
        [console_scripts]
        cffconvert=cffconvert:cli
    """,
    version=__version,
    description='Read CFF formatted CITATION file from a GitHub url or local ' +
                'file and convert it to BibTeX, EndNote, RIS, Codemeta, ' +
                '.zenodo.json, or plain JSON',
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
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
    ],
    packages=find_packages(),
    install_requires=['PyYAML==3.12', 'requests==2.18.4', 'urllib3==1.22', 'click==6.7'],
    setup_requires=['pytest', 'pytest-runner'],
    tests_require=['pytest', 'pytest-runner'],
    long_description=long_description
)
