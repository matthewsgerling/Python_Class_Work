import unittest
from Week8.Collections.set_memberships import in_set


class TestList(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(in_set({1, 2, 3, 4, 5}, 3))

    def test_set_False(self):
        self.assertFalse(in_set({1, 2, 3, 4, 5}, 0))
