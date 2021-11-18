"""History Calculator class Testing"""
import pytest
from calc.history.calculation import Calculations
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication


# pylint: disable=line-too-long

@pytest.fixture
def clear_history_fixture():
    """ Clear history fixure"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def addition_fixture():
    """ Addition fixture"""
    # pylint: disable=redefined-outer-name
    values = (4, 5)
    addition = Addition(values)
    Calculations.add_calculation(addition)


@pytest.fixture
def multiplication_fixture():
    """ Multiple fixure"""
    # pylint: disable=redefined-outer-name
    values = (5, 2)
    multiplication = Multiplication(values)
    Calculations.add_calculation(multiplication)


def add_calculation_history():
    """Add value to history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 9


def query_first_object(clear_history_fixture, multiplication_fixture):
    """Query First calculation from the history"""
    # pylint: disable=line-too-long
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_first_calculation(), Addition)

def query_count_history(clear_history_fixture, addition_fixture):
    """Query number of items from history"""
    # pylint: disable=line-too-long
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1


def test_clear_calculation_history(clear_history_fixture, addition_fixture):
    """Count and Clear History"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True


def query_specific_calculation():
    """Query a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 9


def query_last_result_value(clear_history_fixture, multiplication_fixture):
    """Query last calculation from the history"""
    # pylint: disable=line-too-long
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_last_calculation_result_value() == 10


def query_first_value(clear_history_fixture, addition_fixture):
    """query first calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 9


def test_history_count(clear_history_fixture, addition_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1


def query_last_object(clear_history_fixture, multiplication_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=line-too-long
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Multiplication)
