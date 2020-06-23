import unittest
from Week8.Collections.set_memberships import in_set


class TestList(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(in_set())

    def test_set_Fase(self):
        self.assertFalse(in_set())
