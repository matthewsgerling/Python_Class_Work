from unittest import mock
from InputOutput.main import averageScores


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert averageScores.average() == 90
