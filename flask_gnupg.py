#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Flask-GnuPG
Author: Eldar Aliiev
Email: e.aliiev@vnmu.edu.ua
"""

__author__ = 'Eldar Aliiev'
__copyright__ = 'Copyright 2017, Eldar Aliiev'
__credits__ = ['Eldar Aliiev']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'Eldar Aliiev'
__email__ = 'e.aliiev@vnmu.edu.ua'
__status__ = 'Production/Stable'

import gnupg


class GnuPG(object):
    """
    Flask extension for work with GnuPG
    """

    def __init__(self, app=None):
        """
        Initialize extension
        :param app: Flask application
        :type app: class
        """
        self.app = app
        self._gpg = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize default extensions configuration and
        setup GnuPG wrapper
        :param app: Flask application
        :type app: class
        """
        app.config.setdefault('GPG_HOME_DIR', '~/.gnupg')
        app.config.setdefault('GPG_BINARY', 'gpg2')
        app.config.setdefault('GPG_KEYRING', None)
        app.config.setdefault('GPG_SECRET_KEYRING', None)
        app.config.setdefault('GPG_KEY_ID', '')
        app.config.setdefault('GPG_PASSPHRASE', '')

        self._gpg = gnupg.GPG(
            gpgbinary=app.config['GPG_BINARY'],
            gnupghome=app.config['GPG_HOME_DIR'],
            keyring=app.config['GPG_KEYRING'],
            secret_keyring=app.config['GPG_SECRET_KEYRING']
        )

    def __getattr__(self, method):
        """
        Call GnuPG wrapper method
        :param method: Method name
        :return: GnuPG wrapper method
        :rtype: function
        """
        if not hasattr(self._gpg, method):
            raise AttributeError('Method "{0:s}" not found in GnuPG wrapper!'.format(method))
        return getattr(self._gpg, method)
