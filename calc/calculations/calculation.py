"""Calculation/Abstract Class"""


class Calculation:
    """ Base calculation abstract class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """ constructor"""
        self.values = Calculation.convert_args_to_list_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ factory method"""
        return cls(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
