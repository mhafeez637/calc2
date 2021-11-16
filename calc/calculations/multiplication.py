"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Multiplaction object"""
    def get_result(self):
        """get results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
