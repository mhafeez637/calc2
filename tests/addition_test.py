"""Addition Testing"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """Addition Testing using static method"""
    #Arrange
    mynumbers = (3.0,4.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 7.0
