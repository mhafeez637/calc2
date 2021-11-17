"""Addition Testing"""
from calc.calculations.division import Division

def test_calculation_multiplication():
    """Addition Testing using static method"""
    # Arrange
    xyz = (2.0, 4.0)

    division = Division(xyz)
    # Act
    # Assert
    assert division.get_result() == 2.0
