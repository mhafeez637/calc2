"""Addition Testing"""
from calc.calculations.division import Division

def test_calculation_multiplication():
    """Addition Testing using static method"""
    # Arrange
    mynumbers = (1.0, 1.0)

    division = Division(mynumbers)
    # Act
    # Assert
    assert division.get_result() == 1.0
