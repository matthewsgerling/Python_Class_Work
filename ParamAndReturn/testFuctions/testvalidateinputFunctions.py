import unittest
from ParamAndReturn.moreFunctions.validateInputsFunctions import scoreInput


class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(scoreInput('Matt'))

    def test_score_input_test_score_valid(self):
        self.assertEqual(scoreInput('Matt', 75))

    def test_score_input_test_score_below_range(self):
        self.assertEqual(scoreInput('Matt', -12))

    def test_score_input_test_score_above_range(self):
        self.assertEqual(scoreInput('Matt', 200))

    def test_test_score_non_numeric(self):
        self.assertEqual(scoreInput('Matt', "iFailed"))

    def test_score_input_invalid_message(self):
        self.assertEqual(scoreInput('Matt', 60, 'You Failed Something'))


if __name__ == '__main__':
    unittest.main()
