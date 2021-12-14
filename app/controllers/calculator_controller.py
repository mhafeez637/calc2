from app.controllers.controller import ControllerBase
from csvmanager.read import Read
from csvmanager.write import Write
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
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())

            # Calling the class to write the user input to csv
            inputvalues = ({'Value 1': value1, 'Value 2': value2, 'Operation': operation, 'Result': result})

            Write.DataFrameToCSVFile(inputvalues)

        df_read = Read.DataFrameFromCSVFile()

        return render_template('result.html', data=df_read.values, value11=value1, value12=value2, operation1=operation, result1=result)

    # return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)

    @staticmethod
    def get():
        return render_template('calculator.html')
