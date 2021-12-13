"""CSV file reader"""
import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile():
        """read CSV file"""
        filename = 'inputvalues.csv'
        path = 'csvfiles'
        full_path = path + '/' + filename

        df = pd.read_csv(full_path)

        return df
