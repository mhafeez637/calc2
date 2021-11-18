"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator
from calc.history.calculation import Calculations

@pytest.fixture
def clear_history_fixture():
    """Clear History fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

def calculator_add_static(clear_history_fixture):
    """Adding numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    xyz_tuple = (1.0, 1.0, 1.0)
    Calculator.add_numbers(xyz_tuple)
    assert Calculator.get_last_result_value() == 3.0

def calculator_multiply_static(clear_history_fixture):
    """Multiplying numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    xyz_tuple = (1.0, 4.0, 2.0)
    Calculator.multiply_numbers(xyz_tuple)
    assert Calculator.get_last_result_value() == 8.0

def calculator_sub_static(clear_history_fixture):
    """Adding numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    xyz_tuple = (5.0, 1.0, 1.0)
    Calculator.subtract_numbers(xyz_tuple)
    assert Calculator.get_last_result_value() == -7.0

def calculator_divide_static(clear_history_fixture):
    """Divid numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    xyz_tuple = (2.0, 48.0)
    Calculator.divide_numbers(xyz_tuple)
    assert Calculator.get_last_result_value() == 24.0
