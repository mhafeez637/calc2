"""Subtraction object Testing"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
        """Testing Subtraction using a static method"""
        #Arrange
        mynumbers = (3.0,2.0,-5.0)
        # Act
        subtraction = Subtraction(mynumbers)
        #Assert
        assert subtraction.get_result == 0.0