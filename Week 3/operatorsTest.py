# Program: stringMethods.py
# Author: Matthew Gerling
# Last date modified: 06/6/2020

import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 1
        b = 1
        self.assertTrue(a == b)

    def test_notequal(self):
        a = 1
        b = 2
        self.assertTrue(a != b)

    def test_greaterThan(self):
        a = 2
        b = 1
        self.assertTrue(a > b)

    def test_lessThan(self):
        a = 1
        b = 2
        self.assertTrue(a < b)

    def test_greaterEqual(self):
        a = 2
        b = 1
        self.assertTrue(a >= b)

    def test_lessEqual(self):
        a = 1
        b = 2
        self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()


