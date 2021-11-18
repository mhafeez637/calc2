"""Testing the Calculator"""
import pytest
from calc.history.calculation import Calculations
from calc.calculations.addition import Addition


@pytest.fixture
def ch_fixture():
    """clear history fixture function"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def addition_fixture():
    """addition fixture"""
    # pylint: disable=redefined-outer-name
    values = (5, 6)
    addition = Addition(values)
    Calculations.add_calculation(addition)


def test_add_calculation_to_history(ch_fixture, addition_fixture):
    """Clear History function test"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1


def test_clear_calculation_history(ch_fixture, addition_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True


def test_get_calculation(ch_fixture, addition_fixture):
    """query a specific value from history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 11


def test_get_calculation_first(ch_fixture, addition_fixture):
    """query last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 11


def test_get_calc_last_result_value(ch_fixture, addition_fixture):
    """query last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 11


def test_history_count(ch_fixture, addition_fixture):
    """query record counts from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1


def test_get_calc_last_result_object(ch_fixture, addition_fixture):
    """query last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Addition)
