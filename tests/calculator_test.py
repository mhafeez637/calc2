"""Calculator Testing"""

import pytest

from calculator.calculator import Calculator

# We define a function that will run each time you pass it to a test which is called a fixture
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture

def calc_history():
    """Testing clear History Method"""
    Calculator.calc_history()

def test_calculator_addition(calc_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(1, 1) == 2
    assert Calculator.add_numbers(6, 8) == 14
    assert Calculator.history_count() == 3
    assert Calculator.get_last_cal_add_hist() == 14

def test_cleary_history(calc_history):
    """Testing Clear History with Add numbers"""
    assert Calculator.add_numbers(1,1) == 2
    assert Calculator.add_numbers(3, 5) == 8
    assert Calculator.history_count() == 2
    assert Calculator.calc_history() is True
    assert Calculator.history_count() == 0

def test_count_history(calc_history):
    """Testing the count history before and after"""
    assert Calculator.history_count() == 0
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(1, 1) == 2
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(calc_history):
    """Testing last result"""
    assert Calculator.add_numbers(1, 1) == 2
    assert Calculator.add_numbers(1, 3) == 4
    assert Calculator.get_last_cal_add_hist() == 4

def test_get_first_calculation_result(calc_history):
    """Testing first number"""
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(3, 2) == 5
    assert Calculator.get_first_cal_add_hist() == 4

def test_calculator_subtract(calc_history):
    """Testing the subtract function"""
    assert Calculator.subtract_numbers(4, 2) == 2
    assert Calculator.subtract_numbers(5, 2) == 3

def test_calculator_multiply(calc_history):
    """ testing multiplication"""
    assert Calculator.multiply_numbers(1, 1) == 1
    assert Calculator.multiply_numbers(2,2) == 4

def test_calculator_division(calc_history):
    """ testing division"""
    assert Calculator.divide_numbers(2, 2) == 1
    assert Calculator.divide_numbers(4, 2) == 2