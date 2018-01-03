#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import flask_gnupg

setup(
    name='Flask-GnuPG',
    version=flask_gnupg.__version__,
    author=flask_gnupg.__author__,
    author_email=flask_gnupg.__email__,
    maintainer=flask_gnupg.__author__,
    maintainer_email=flask_gnupg.__email__,
    url='https://github.com/EldarAliiev/flask-gnupg',
    download_url='https://github.com/EldarAliiev/flask-gnupg/archive/master.zip',
    license=flask_gnupg.__license__,
    description='Flask extension for work with GnuPG',
    long_description=open('README.rst').read(),
    py_modules=['flask_gnupg'],
    python_requires='>=3.4',
    install_requires=[
        'Flask>=0.12.2',
        'python-gnupg>=0.4.1',
    ],
    tests_require=[
        'tox',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: %s License' % flask_gnupg.__license__,
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'Flask',
        'GnuPG',
        'PGP',
    ],
    test_suite='tests',
    zip_safe=False,
    include_package_data=True
)
