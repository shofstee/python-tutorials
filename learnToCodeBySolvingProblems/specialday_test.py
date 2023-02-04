import unittest
from specialday import *


class SpecialDay(unittest.TestCase):
    def test_something(self):
        self.assertEqual('Before', is_special_day(1, 1))
        self.assertEqual('Before', is_special_day(2, 1))
        self.assertEqual('Special', is_special_day(2, 18))
        self.assertEqual('After', is_special_day(2, 19))
        self.assertEqual('After', is_special_day(3, 1))

if __name__ == '__main__':
    unittest.main()
