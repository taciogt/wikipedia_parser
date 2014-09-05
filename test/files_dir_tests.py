# -*- coding: utf8 -*-

__author__ = 'tacio'


import unittest
import os

from file_paths import WIKI_DUMP


class TestCharacterFormatting(unittest.TestCase):

    def test_check_dump_file(self):
        self.assertTrue(os.path.isfile(WIKI_DUMP))
        self.assertEqual(4868697939, os.path.getsize(WIKI_DUMP))