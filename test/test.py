import unittest
from evaluate import *

class TestBinaryOperators(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(evaluate('(+ 3 4)'), 7)
        self.assertEqual(evaluate('(+ (+ 1 2) 2)'), 5)


if __name__ == '__main__':
    unittest.main()