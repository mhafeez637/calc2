"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator
from calc.history.calculation import Calculations


@pytest.fixture
def ch_fixture():
    """Clear History fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


def test_add_static_calculator(ch_fixture):
    """Testing static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args
    tuple_value = (4, 1, 9)
    Calculator.add_numbers(tuple_value)
    assert Calculator.get_last_result_value() == 14.0


def test_subtract_static_calculator(ch_fixture):
    """Testing static method for subtract"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args
    tuple_value = (4, 0, 3)
    Calculator.subtract_numbers(tuple_value)
    assert Calculator.get_last_result_value() == -7.0


def test_calculator_multiply_static(ch_fixture):
    """Testing static method for Multiply"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args
    tuple_value = (5, 5, 1)
    Calculator.multiply_numbers(tuple_value)
    assert Calculator.get_last_result_value() == 25.0

def test_calculator_divide_static(ch_fixture):
    """Testing static method for divide"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args
    tuple_value = (2, 4)
    Calculator.divide_numbers(tuple_value)
    assert Calculator.get_last_result_value() == 2.0
