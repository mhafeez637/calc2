"""History Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculations:
    """History Aray"""
    history = []

    @staticmethod
    def readHistoryFromCSV():
        """Read the history from csv and put it into the history """
    @staticmethod
    def writeHistoryToCSV():
        """Write the history to csv file"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clear History Class"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Query number of items from history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Query last item from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """Query last calculation from history"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """Query first calculation from history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ Query a specific item from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ Query a calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Add an object to history"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """subtraction an object to history"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Multiplication an object to history"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Division an object to history"""
        Calculations.add_calculation(Division.create(values))
        return True
