import unittest
from Week8.Collections.dict_membership import in_dict


class TestList(unittest.TestCase):
    def test_set_true(self):
        self.assertTrue(in_dict())

    def test_set_False(self):
        self.assertFalse(in_dict())
