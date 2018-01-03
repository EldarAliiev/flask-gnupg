Flask-GnuPG
==============

.. image:: https://img.shields.io/pypi/v/flask-gnupg.svg
    :target: https://pypi.python.org/pypi/flask-gnupg

.. image:: https://img.shields.io/pypi/l/flask-gnupg.svg
    :target: https://raw.githubusercontent.com/EldarAliiev/flask-gnupg/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/flask-gnupg.svg
    :target: https://pypi.python.org/pypi/flask-gnupg

.. image:: https://img.shields.io/pypi/wheel/flask-gnupg.svg
    :target: https://pypi.python.org/pypi/flask-gnupg

.. image:: https://img.shields.io/pypi/status/flask-gnupg.svg
    :target: https://pypi.python.org/pypi/flask-gnupg

.. image:: https://travis-ci.org/EldarAliiev/flask-gnupg.svg?branch=master
    :target: https://travis-ci.org/EldarAliiev/flask-gnupg

.. image:: https://coveralls.io/repos/github/EldarAliiev/flask-gnupg/badge.svg?branch=master
    :target: https://coveralls.io/github/EldarAliiev/flask-gnupg?branch=master

.. image:: https://img.shields.io/github/contributors/EldarAliiev/flask-gnupg.svg
    :target: https://github.com/EldarAliiev/flask-gnupg/graphs/contributors



Flask extension for work with GnuPG based on python-gnupg.

https://github.com/EldarAliiev/flask-gnupg

Install:
--------

.. code-block:: bash

    $ git clone https://github.com/EldarAliiev/flask-gnupg.git
    $ cd flask-gnupg
    $ python setup.py install

or with pip:

.. code-block:: bash

    $ pip install Flask-GnuPG

Usage example:
--------------

Set up configuration in your Flask application:

* **GPG_HOME_DIR** : default **'~/.gnupg'**
* **GPG_BINARY** : default **'gpg2'**
* **GPG_KEYRING** : default **None**
* **GPG_SECRET_KEYRING** : default **None**
* **GPG_KEY_ID** : default **''**
* **GPG_PASSPHRASE** : default **''**

Create the application and initialize GnuPG instance:

.. code-block:: python

    from flask import Flask
    from flask_gnupg import GnuPG

    app = Flask(__name__)
    gpg = GnuPG(app)

Or you can set up GnuPG instance later:

.. code-block:: python

    gpg = GnuPG()

    app = Flask(__name__)
    gpg.init_app(app)

Then you can use GnuPG engine in your views:

.. code-block:: python

    @app.route('/')
    def index():
        keys_list = gpg.list_keys()
        return keys_list

For details about all allowed methods read the docs of `python-gnupg <http://pythonhosted.org/python-gnupg/>`_ library.
