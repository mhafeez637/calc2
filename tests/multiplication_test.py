"""multiplication object Testing"""
from calc.calculations.multiplication import Multiplication


def test_calculation_division():
    """multiplication testing using a static method"""
    # Arrange
    xyz = (2.0, 2.0)
    # Act
    multiplication = Multiplication(xyz)
    # Assert
    assert multiplication.get_result() == 4.0
