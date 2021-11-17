"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ calculation object"""
    def get_result(self):
        """get results"""
        total = 1.0
        for value in self.values:
            total = value / total
        return total
