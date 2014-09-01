# -*- coding: utf8 -*-

__author__ = 'tacio'


import unittest
import formatter


class TestCharacterFormatting(unittest.TestCase):

    def test_italic(self):
        text = "Some text with ''italic chars''. End."
        formatted_text = "Some text with italic chars. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Some text with ''italic chars'' and ''another formatted words''. End."
        formatted_text = "Some text with italic chars and another formatted words. End."
        self.assertEqual(formatted_text, formatter.format_text(text))


    def test_bold(self):
        text = "Some text with '''bold chars'''. End."
        formatted_text = "Some text with bold chars. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Some text with '''bold chars''' and some more '''strong words'''. End."
        formatted_text = "Some text with bold chars and some more strong words. End."
        self.assertEqual(formatted_text, formatter.format_text(text))


    def test_bold_and_italic(self):
        text = "Some text with '''''bold and italic chars'''''. End."
        formatted_text = "Some text with bold and italic chars. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Some text with '''''bold and italic chars''''' and '''''another'''''. End."
        formatted_text = "Some text with bold and italic chars and another. End."
        self.assertEqual(formatted_text, formatter.format_text(text))


    def test_strike_text(self):
        text = "Some text with <strike>striked chars</strike>. End."
        formatted_text = "Some text with striked chars. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Some text with <strike>striked chars</strike> and <strike>doubled</strike>. End."
        formatted_text = "Some text with striked chars and doubled. End."
        self.assertEqual(formatted_text, formatter.format_text(text))


    def test_escape_wiki_markup(self):
        text = "Some text with <nowiki>no ''markup''</nowiki>. End."
        formatted_text = "Some text with no ''markup''. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Checking if escapes <nowiki>some '''bold markup'''</nowiki>. End."
        formatted_text = "Checking if escapes some '''bold markup'''. End."
        self.assertEqual(formatted_text, formatter.format_text(text))

        text = "Checking if escapes <nowiki>some <strike>no strike</strike> markup</nowiki>. End."
        formatted_text = "Checking if escapes some <strike>no strike</strike> markup. End."
        self.assertEqual(formatted_text, formatter.format_text(text))