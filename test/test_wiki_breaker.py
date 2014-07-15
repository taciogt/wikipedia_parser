__author__ = 'tacio'


import random
import unittest
import os


class TestWikiBreaker(unittest.TestCase):

    @staticmethod
    def _clean_created_test_files():
        print 'Cleaning created files...'
        file_name = __file__.split(os.path.sep)[-1]
        file_dir = __file__.replace(file_name, '')
        created_files_dir = os.path.join(file_dir, 'files', 'created', 'articles-files')
        for f in os.listdir(created_files_dir):
            f = os.path.join(created_files_dir, f)
            print 'Removing file: ' + f
            os.remove(f)

    @classmethod
    def setUpClass(cls):
        cls._clean_created_test_files()

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

# if __name__ == '__main__':
#     unittest.main()