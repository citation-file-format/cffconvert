#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from distutils.util import convert_path


def get_install_dependencies():
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
    return [line.rstrip('\n') for line in lines]


def get_test_dependencies():
    with open("requirements-dev.txt", "r") as f:
        lines = f.readlines()
    return [line.rstrip('\n') for line in lines]


def get_readme():
    with open("README.rst", "r") as f:
        return f.read()


def get_version():
    # https://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in
    # -my-package#answer-24517154
    version_namespace = {}
    version_path = convert_path('cffconvert/version.py')
    with open(version_path) as version_file:
        exec(version_file.read(), version_namespace)
    return version_namespace["__version__"]

setup(
    name='cffconvert',
    py_modules=["cffconvert"],
    entry_points="""
        [console_scripts]
        cffconvert=cffconvert:cli
    """,
    version=get_version(),
    description='Read CFF formatted CITATION file from a GitHub url or local ' +
                'file and convert it to BibTeX, EndNote, RIS, Codemeta, ' +
                '.zenodo.json, or plain JSON',
    author='Jurriaan H. Spaaks',
    author_email='j.spaaks@esciencecenter.nl',
    license='Apache 2.0',
    url='https://github.com/citation-file-format/cff-converter-python',
    download_url='https://github.com/citation-file-format/cff-converter-python/archive/%s.tar.gz' % get_version(),
    include_package_data=True,
    keywords=['citation', 'cff', 'CITATION.cff', 'bibliography'],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    install_requires=get_install_dependencies() + get_test_dependencies(),
    long_description=get_readme()
)
