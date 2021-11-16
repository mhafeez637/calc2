"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ calculation object"""
    def get_result(self):
        """get results"""
        division_value = 1.0
        for value in self.values:
            division_value = value / division_value
        return division_value
