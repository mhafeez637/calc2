"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator
from calc.history.calculation import Calculations

@pytest.fixture
def clear_history_fixture():
    """Clear History fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """Adding numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0,1.0,1.0) == 3.0

def test_calculator_multiply_static(clear_history_fixture):
    """Multiplying numbers using a static method"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0
