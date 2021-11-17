"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Multiplaction object"""
    def get_result(self):
        """get results"""
        total = 1.0
        for value in self.values:
            total = total * value
        return total
