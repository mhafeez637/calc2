"""This is the increment function"""


class Calculator:
    """This is the Calculator class"""

    result = 0

    def get_result(self):
        """Get Result of Calculation"""
        return self.result

    def add_function(self, value_a, value_b):
        """Add two num_bers and store the result"""
        self.result = value_a + value_b
        return self.result

    def subtract_function(self, value_a, value_b):
        """Subtract two num_bers and store the result"""
        self.result = value_a - value_b
        return self.result

    def multiply_function(self, value_a, value_b):
        """Multiply two num_bers and store the result"""
        self.result = value_a * value_b
        return self.result

    def division_function(self, value_a, value_b):
        """divide two num_bers and store the result"""
        self.result = value_a / value_b
        return self.result
