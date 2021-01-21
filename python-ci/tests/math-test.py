import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.math import addition


class MathTest(unittest.TestCase):
    def test_addition(self):
        actual = addition(4, 4)
        expected = 8
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
