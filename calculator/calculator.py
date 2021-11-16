"""This is the increment function"""

from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculation import Calculations


class Calculator:
    """ Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result

    @staticmethod
    def multiply_numbers(*args):
        """Multiply numbers  from result"""
        # Multiplication object
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def divide_numbers(*args):
        """Divide numbers from result"""
        # Division object
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
