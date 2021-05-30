#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'pylisk'
DESCRIPTION = 'Starter Kit to develop a Python library'
URL = 'https://github.com/adbeda/pylib-starter'
EMAIL = 'at@gmail.com'
AUTHOR = '#'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = 0.1

with open("README.md") as f:
    long_description = f.read()

REQUIRED = [
    'pillow',
    'click',
    'numpy'
]

EXTRA_REQUIRED = {
    'test': ['mock',
             'pytest',
             'pytest-cov',
             'codecov'],
    'dev': ['pytest',
            'pytest-cov',
            'pre-commit']}

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests')),
    install_requires=REQUIRED,
    extras_require=EXTRA_REQUIRED,
    include_package_data=True,
    license='MIT',
    entry_points='''
             [console_scripts]
                 ''',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)