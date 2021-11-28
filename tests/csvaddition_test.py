from calculator.calculator import Calculator
from calc.history.calculation import Calculations

# Load the Pandas libraries with alias 'pd'
import pandas as pd
import pytest
"""Testing the Calculator"""
def test_add_static_calculator():
    """Testing static method for addition"""
    #Read csv file as external data load
    data = pd.read_csv('tests/test_data/addition.csv')
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args
    tuple_value = data.value_1[0], data.value_2[0]
    Calculator.add_numbers(tuple_value)
    assert Calculator.get_last_result_value() == data.result[0]
