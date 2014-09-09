# -*- coding: utf8 -*-

__author__ = 'tacio'


import unittest
import markup_formatter


class TestSectionFormatting(unittest.TestCase):

    def test_levels(self):
        text = """Some introduction.
==Level 2==
End."""
        formatted_text = """Some introduction.
Level 2
End."""
        self.assertEqual(formatted_text, markup_formatter.format_text(text))