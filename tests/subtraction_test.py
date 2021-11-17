"""Subtraction Testing"""
from calc.calculations.subtraction import Subtraction


def test_calculation_subtraction():
    """Subtraction Testing using static method"""
    # Arrange
    xyz = (1.0, 1.0)

    subtraction = Subtraction(xyz)
    # Act
    # Assert
    assert subtraction.get_result() == -2.0
