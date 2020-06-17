import unittest
from inputValidation.main.validationWithTry import average


def test_average_exception(self):
    with self.assertRaise(ValueError):
        try:
            print(average(-90, -89, 78))
        except ValueError:
            raise ValueError('Value error')
        else:
            print('Unexpected fail')
        finally:
            pass
