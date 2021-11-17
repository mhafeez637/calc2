"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation object"""
    def get_result(self):
        """get results"""
        total = 0.0
        for value in self.values:
            total = value + total
        return total
