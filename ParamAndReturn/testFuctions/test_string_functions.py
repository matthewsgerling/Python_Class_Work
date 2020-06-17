import unittest
from ParamAndReturn.moreFunctions.stringfunctions import multiplyString


class FunctionTestCase(unittest.TestCase):
    def test_multiple_String(self):
        multiplyString('Ayah', 4)

