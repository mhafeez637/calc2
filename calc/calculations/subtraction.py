"""Subtraction Class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """ calculation object"""
    def get_result(self):
        """get results"""
        total = 0.0
        for value in self.values:
            total = total - value
        return total
