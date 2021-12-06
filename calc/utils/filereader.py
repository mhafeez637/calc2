"""external file reader"""
import os
import pandas as pd

class PandasFileReader:
    """Panda file reader class"""
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    def read_file(self):
        function_handler = None
        if ".csv" in self.file_name:
            function_handler = self._process_csv_file
        else:
            raise ValueError("Don't find any CSV file")
        return function_handler()

    def _process_csv_file(self):
        """CSV file reader Method"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/test_data", self.file_name)
        df_data = pd.read_csv(file_path, header=None)
        return df_data