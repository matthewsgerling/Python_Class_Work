import unittest
from Module2.main import camperAgeInput


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(camperAgeInput.convert_to_months(3), 36)


if __name__ == '__main__':
    unittest.main()