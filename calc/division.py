"""Division Calculation from values A and value B in the calculation class"""

from calc.calculation import Calculation


# Multiplication class child class
class Division(Calculation):
    """value_a and value_b result get from calculation class"""

    def get_result(self):
        """return encapsulation."""
        return self.value_a / self.value_b
