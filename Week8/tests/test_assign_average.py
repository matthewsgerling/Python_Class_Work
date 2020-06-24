import unittest
from Week8.Collections.assign_average import switch_average


class TestList(unittest.TestCase):
    def testA(self):
        self.assertTrue(switch_average('a'))

    def testB(self):
        self.assertTrue(switch_average("b"))

    def testE(self):
        self.assertTrue(switch_average('e'))

    def testC(self):
        self.assertTrue(switch_average('c'))

    def testD(self):
        self.assertTrue(switch_average('d'))
