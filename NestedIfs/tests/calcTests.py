from unittest import mock
from NestedIfs.main import couponCalculations


def test_price_under_ten(self):
    with mock.patch('builtins.input'):
        assert couponCalculations.calculate_price(5, 5, 10)
        assert couponCalculations.calculate_price(5, 5, 15)
        assert couponCalculations.calculate_price(5, 5, 20)
        assert couponCalculations.calculate_price(5, 10, 10)
        assert couponCalculations.calculate_price(5, 10, 15)
        assert couponCalculations.calculate_price(5, 10, 20)


def test_price_under_between_ten_thirty(self):
    with mock.patch('builtins.input'):
        assert couponCalculations.calculate_price(15, 5, 10)
        assert couponCalculations.calculate_price(15, 5, 15)
        assert couponCalculations.calculate_price(15, 5, 20)
        assert couponCalculations.calculate_price(15, 10, 10)
        assert couponCalculations.calculate_price(15, 10, 15)
        assert couponCalculations.calculate_price(15, 10, 20)


def test_price_under_between_thirty_fifty(self):
    with mock.patch('builtins.input'):
        assert couponCalculations.calculate_price(40, 5, 10)
        assert couponCalculations.calculate_price(40, 5, 15)
        assert couponCalculations.calculate_price(40, 5, 20)
        assert couponCalculations.calculate_price(40, 10, 10)
        assert couponCalculations.calculate_price(40, 10, 15)
        assert couponCalculations.calculate_price(40, 10, 20)


def test_price_under_over_fifty(self):
    with mock.patch('builtins.input'):
        assert couponCalculations.calculate_price(60, 5, 10)
        assert couponCalculations.calculate_price(60, 5, 15)
        assert couponCalculations.calculate_price(60, 5, 20)
        assert couponCalculations.calculate_price(60, 10, 10)
        assert couponCalculations.calculate_price(60, 10, 15)
        assert couponCalculations.calculate_price(60, 10, 20)