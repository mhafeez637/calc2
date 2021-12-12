import os
import pandas as pd

class Write:

    def __init__(self, data):
        self._data = data

    @property
    def input_value1(self):
        return self._data

    @staticmethod
    def DataFrameToCSVFile(self):

        df= pd.DataFrame([self._data], columns=['value1', 'value2', 'operation'])
        inputfile = df.to_csv('csvfiles/inputvalues.csv', mode='a', header=not os.path.exists('csvfiles/inputvalues.csv'))
        return inputfile
