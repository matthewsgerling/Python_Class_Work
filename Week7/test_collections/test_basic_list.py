import unittest
from unittest.mock import patch
import Week7.fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('Week7.fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])

    @patch('Week7.fun_with_collections.basic_list_extenction.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            topic1.make_list()  # call the function!

    def test_make_list_below_range(self):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            try:
                topic1.make_list()  # call the function!
            except ValueError:
                print("error")

    def test_make_list_above_range(self):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            try:
                topic1.make_list()  # call the function!
            except ValueError:
                print("error")




