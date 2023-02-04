import unittest
from spookyseason import *


class SpookeySeasonTestCase(unittest.TestCase):

    def test_calculate_spookines(self):
        self.assertEqual('spooooky', calculate_spookines(4))

if __name__ == '__main__':
    unittest.main()
