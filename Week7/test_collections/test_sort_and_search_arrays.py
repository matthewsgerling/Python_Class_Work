import unittest

from Week7.fun_with_collections import sort_and_search_arrays


class TestList(unittest.TestCase):
    def test_sort(self):
        sort_and_search_arrays.sortArray(['h', 'p', 'o', 'm'])

    def test_sort(self):
        sort_and_search_arrays.searchArray(['h', 'p', 'o', 'm'], 'h')

    def test_sort(self):
        sort_and_search_arrays.searchArray(['h', 'p', 'o', 'm'], 'n')
