"""Addition Testing"""
from calc.calculations.addition import Addition


def test_calculation_addition():
    """Addition Testing using static method"""
    # Arrange
    xyz = (3.0, 4.0)

    # Act
    addition = Addition(xyz)

    # Assert
    assert addition.get_result() == 7.0
