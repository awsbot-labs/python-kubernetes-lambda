#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    no description available

    :copyright: (c) 2020 by awsbot-labs.
    :license: see LICENSE for more details.
"""

import codecs
import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Taken from pypa pip setup.py:
    intentionally *not* adding an encoding option to open, See:
       https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    """
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='lambdakube',
    version=find_version("lambdakube/__init__.py"),
    description='Bootstrapping tool for AWS EKS clusters.',
    long_description=read('README.md'),
    classifiers=[
        ],
    author='awsbot-labs',
    author_email='',
    url='',
    packages=[
        'lambdakube'
        ],
    package_data={'lambdakube': ['fluentd/*.conf']},
    platforms='any',
    license='LICENSE',
    install_requires=[
        'botocore==1.16.19',
        'boto3==1.13.19',
        'kubernetes==11.0.0',
        'PyYAML==5.3.1',
        'jinja2==2.11.2'
    ],
)
