import os

import pandas as pd
from csv import writer
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            Calculator.getHistoryFromCSV()
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)

            result = str(Calculator.get_last_result_value())
            my_dict = {
                'value1': [value1],
                'value2': [value2],
                'operation': [operation]
            }
            df = pd.DataFrame(my_dict)
            df.to_csv('csvfiles/inputvalues.csv', mode='a', header=not os.path.exists('csvfiles/inputvalues.csv'))

            return render_template('result.html', data=Calculator.getHistory(), value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')