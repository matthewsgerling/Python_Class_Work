import unittest

from Week8.Collections.datetime import half_birthday
import _datetime


class TestList(unittest.TestCase):
    def testDate(self):
        with self.assertRaise(ValueError):
            assert half_birthday(_datetime.datetime(2020, 4, 23))

