"""Calculation history Class"""
class Calculations:
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """ Clear history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """ Count history records"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """ Call Last record from history"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """ call first record from history"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ Call a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ Call a specific calculation from history"""
        return Calculations.history.append(calculation)
