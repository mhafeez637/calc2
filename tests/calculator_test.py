"""Testing the Calculator"""
from calculator.calculator import Calculator


def test_calculator_result():
    """Testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    result = calc.add_function(1, 1)
    assert result == 2


def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    result = calc.subtract_function(9, 4)
    assert result == 5

def test_calculator_multiply():
    """Testing  multiplication of two numbers"""
    calc = Calculator()
    result = calc.multiply_function(7, 2)
    assert result == 14

def test_calculator_division():
    """Testing  Division of two numbers"""
    calc = Calculator()
    result = calc.division_function(4, 2)
    assert result == 2
