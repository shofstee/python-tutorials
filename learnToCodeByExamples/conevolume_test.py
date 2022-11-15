import unittest
from conevolume import *


class ConeVolumeTestCase(unittest.TestCase):

    def test_calculate_cone_volume(self):
        self.assertEqual(100.53096491487338, calculate_cone_volume(4, 6))

if __name__ == '__main__':
    unittest.main()
