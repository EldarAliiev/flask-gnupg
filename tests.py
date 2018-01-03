#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from flask import Flask
from flask_gnupg import GnuPG


class TestGnuPG(unittest.TestCase):

    TESTING = True

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(self)
        self.assertTrue(self.app.testing)
        self.gpg = GnuPG(self.app)
        self.ctx = self.app.test_request_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_version(self):
        self.assertIsInstance(self.gpg.version, tuple)

    def test_list_keys(self):
        self.assertIsInstance(self.gpg.list_keys(), list)

    def test_invalid_method(self):
        with self.assertRaises(AttributeError):
            self.gpg.unknown_method()
