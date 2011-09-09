#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Jason Davies
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'CouchDB-MailDir-FUSE',
    version = '0.1',
    description = 'CouchDB MailDir FUSE module',
    long_description = \
"""This is a Python FUSE module for CouchDB. It allows a CouchDB database
to be mounted on a virtual filesystem and read as a MailDir folder.""",
    author = 'Théodore Biadala',
    author_email = 'theodore@biadala.net',
    license = 'BSD',
    url = '',
    zip_safe = True,

    py_modules = ['couchmount'],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
    ],

    entry_points = {
        'console_scripts': [
            'couchmount = couchmount:main',
        ],
    },

    install_requires = ['CouchDB>=1.0'],
)
