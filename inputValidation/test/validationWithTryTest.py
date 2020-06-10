import unittest
from inputValidation.main import validationWithTry
from inputValidation.main.validationWithTry import average


def test_average_exception(self):
    with self.assertRaises(ValueError):
        print(average(-90, 89, 78))
        
