import unittest

from Week7.fun_with_collections.sort_and_search_list import sortList
from Week7.fun_with_collections.sort_and_search_list import searchList


class TestList(unittest.TestCase):
    def test_sort(self):
        with self.assertRaises(ValueError):
            sortList(['h', 'p', 'o', 'm'])

    def test_search(self):
        with self.assertRaises(ValueError):
            searchList(['h'], ['h', 'p', 'o', 'm'])
