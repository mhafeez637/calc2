"""This is the increment function"""

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division


class Calculator:
    """ This is the Calculator class for clear history"""
    # Calculator static property
    history = []

    @staticmethod
    def get_first_cal_add_hist():
        """Get the first added calculation history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def cl_hist():
        """Clears history from calculator"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """History count for the calculations"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """store calculation history to calculator"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_last_cal_add_hist():
        """Last added value to calculation history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_number(value_a, value_b):
        """Add two numbers"""
        # Addition object
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_cal_add_hist()

    @staticmethod
    # Calling method
    def subtract_number(value_a, value_b):
        """Subtract two numbers"""
        # Subtraction object
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_cal_add_hist()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """Multiply two numbers"""
        # Multiplication object
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_last_cal_add_hist()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """Divide two numbers"""
        # Division object
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_last_cal_add_hist()
