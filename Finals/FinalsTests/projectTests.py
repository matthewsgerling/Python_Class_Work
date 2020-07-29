# Name: Matthew Gerling
# File: projectTests

import unittest
from Finals.Finalprogect.vimeoApp import VimeoAPI


class Tests(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.vimeo = VimeoAPI()

    def test_Folder_true(self):
        self.assertTrue(VimeoAPI.list_folder(self.vimeo, 'Baseball'))

    def test_Folder_false(self):
        self.assertFalse(VimeoAPI.list_folder(self.vimeo, 'football'))

    def test_Get_folder_return(self):
        with self.assertRaise(ValueError):
            try:
                folder = "baseball"
                videos = VimeoAPI.list_folder(folder)
                print(videos)

            except ValueError:
                print('Could not get list')
