import os

import pandas as pd
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'The values cannot be empty'
            return render_template('calculator.html', error=error)
        else:

            flash('Calculation was successful')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            inputvalues = ({'Value 1': value1, 'Value 2': value2, 'Operation': operation})

            my_tuple = (value1, value2)

            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)

            result = str(Calculator.get_last_result_value())

            # Calling the class to write the user input to csv
            df = pd.DataFrame([inputvalues])
            df.to_csv('csvfiles/inputvalues.csv', mode='a', header=not os.path.exists('csvfiles/inputvalues.csv'))

            df = pd.read_csv('csvfiles/inputvalues.csv')


            return render_template('result.html', data=df.values)




    @staticmethod
    def get():
        return render_template('calculator.html')