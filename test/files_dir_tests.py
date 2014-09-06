# -*- coding: utf8 -*-

__author__ = 'tacio'


import unittest
import os

from file_paths import ROOT, WIKI_DUMP, PAGES_DIR


class TestCharacterFormatting(unittest.TestCase):

    def test_check_dump_file(self):
        self.assertTrue(os.path.isfile(WIKI_DUMP))
        self.assertEqual(4868697939, os.path.getsize(WIKI_DUMP))


    def test_check_pages_dir(self):
        self.assertTrue(os.path.isdir(PAGES_DIR))


    def test_no_unnecessary_files_and_dirs(self):
        entities = os.listdir(ROOT)
        self.assertEqual(2, len(entities))