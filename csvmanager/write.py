import os
import pandas as pd

class Write:
    @staticmethod

    def DataFrameToCSVFile(inputvalues):

        df= pd.DataFrame([inputvalues])
        inputfile=df.to_csv('csvfiles/inputvalues.csv', mode='a', header=not os.path.exists('csvfiles/inputvalues.csv'))
        return inputfile
