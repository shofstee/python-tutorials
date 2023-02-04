import unittest
from wordcount import *


class WordCountTestCase(unittest.TestCase):

    def test_wordcount(self):
        self.assertEqual(4, wordcount("dit is een test"))

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(4, wordcount("   dit is een test  "))

    def test_extra_spacing_in_the_middle(self):
        self.assertEqual(4, wordcount("dit is   een test"))

    def test_empty_string(self):
        self.assertEqual(0, wordcount(""))

    def test_null_string(self):
        self.assertEqual(0, wordcount(None))


if __name__ == '__main__':
    unittest.main()
