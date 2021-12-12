""" This is the calculator controller class"""
from flask import render_template, request, flash, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator


class CalculatorController(ControllerBase):
    """This class controls the operation of the calculator"""
    @staticmethod
    def post():
        """This method deals with the validation of operations"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a valid entry for value 1 and or value 2'
        else:
            Calculator.getHistoryFromCSV()
            flash('Calculation has done. What Next')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            # Hey if you copy this it will not work you need to think about it
            data = {
                'value1': [value1],
                'value2': [value2],
                'operation': [operation]
            }
            Calculator.writeHistoryToCSV()
            return render_template('result.html', data=Calculator.getHistory(),
                                   value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """ This method returns the template back to calculator controller class"""
        return render_template('calculator.html')