"""Testing the Calculator"""
import pytest
from calc.history.calculation import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """Clear History fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

@pytest.fixture
def addition_calculation_fixture():
    """ addition function without clear history for reference value"""
    # pylint: disable=redefined-outer-name
    values = (1, 1)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def query_calculation_first(clear_history_fixture, addition_calculation_fixture):
    """calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 2.0

def query_calculation_specific(clear_history_fixture, addition_calculation_fixture):
    """Query Specific calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(1).get_result() == 2.0
