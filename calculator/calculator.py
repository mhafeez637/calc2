""" Increment Function"""
from calc.history.calculation import Calculations


# Calculator class methods to calculate Add, sub, multiply and division
class Calculator:
    """ Calculator class"""

    # Calculator class
    @staticmethod
    def get_last_result_value():
        """ Get Result"""
        # This to have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    # Using Tuple
    def add_numbers(tuple_values: tuple):
        """ Addition"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ Subtraction"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ Multiply"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Division"""
        Calculations.add_division_calculation(tuple_values)
        return True
    @staticmethod
    def getHistory():
        """ Get history """
        return Calculations.history
    @staticmethod
    def getHistoryFromCSV():
        """ Get history """
        return Calculations.readHistoryFromCSV()
    @staticmethod
    def writeHistoryToCSV():
        """ Get history """
        return Calculations.writeHistoryToCSV()
