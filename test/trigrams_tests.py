# -*- coding: utf8 -*-

__author__ = 'tacio'

import unittest


from corpus_analyzer import get_trigrams


class TestTrigramsSaving(unittest.TestCase):

    def test_check_three_words(self):
        text = 'Just three words'
        self.assertTupleEqual(get_trigrams(text)[0], ('Just', 'three', 'words'))

    def test_check_three_words_in_phrase(self):
        text = 'Just three words.'
        self.assertListEqual(get_trigrams(text), [('Just', 'three', 'words')])

    def test_check_four_words_in_phrase(self):
        text = 'Now with four words.'
        self.assertListEqual(get_trigrams(text), [('Now', 'with', 'four'), ('with', 'four', 'words')])

    def test_check_six_words_in_phrase(self):
        text = 'Now with more than four words.'
        trigrams = get_trigrams(text)

        self.assertEqual(len(trigrams), 4)
        self.assertTupleEqual(trigrams[0], ('Now', 'with', 'more'))
        self.assertTupleEqual(trigrams[1], ('with', 'more', 'than'))
        self.assertTupleEqual(trigrams[2], ('more', 'than', 'four'))
        self.assertTupleEqual(trigrams[3], ('than', 'four', 'words'))
