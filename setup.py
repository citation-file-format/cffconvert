#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version = '1.0.0'

setup(
    name='citationcff',
    version=__version,
    description='Read CFF formatted CITATION file from a GitHub url and convert it to BibTex, EndNote, and RIS',
    author='Jurriaan Spaaks',
    author_email='j.spaaks@esciencecenter.nl',
    license='Apache 2.0',
    url='https://github.com/citationcff/citationcff',
    download_url='https://github.com/citationcff/citationcff/archive/%s.tar.gz' % __version,
    include_package_data=True,
    keywords=['citation', 'cff', 'citationcff', 'bibliography'],
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
Read CFF formatted CITATION file from a GitHub url and convert it to BibTex, EndNote, and RIS
---------------------------------------------

Does not support the full CFF spec yet."""
)
