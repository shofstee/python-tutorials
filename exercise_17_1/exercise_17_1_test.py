import unittest
from exercise_17_1 import GithubRepositoriesPrinter

class MyTestCase(unittest.TestCase):
    def test_status_code(self):
        printer = GithubRepositoriesPrinter()
        data = printer.get_data()
        self.assertEqual(200, printer.status_code)  # add assertion here


if __name__ == '__main__':
    unittest.main()
