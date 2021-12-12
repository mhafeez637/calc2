"""Testing CSV Read and Write Functionalities"""
import os.path
import pandas
import pandas as pd
from csvmanager.write import Write
from csvmanager.read import Read


def test_write_csv():
    """This is a test to write the addition calculation results"""
    # Arrange
    filename = 'addition.csv'
    path = 'tests/test_data'
    full_path = path + '/' + filename
    name_dict = {
        'value1': ['2', '11', '2', '3.0'],
        'value2': ['3.0', '1.0', '3.0', '4.0'],
        'result': [5, 12, 5, 7.0]
    }
    os.remove(full_path)
    df = pd.DataFrame(name_dict)
    # Act
    Write.DataFrameToCSVFile(full_path, df)
    # Assert
    assert os.path.exists(full_path)


def test_read_csv():
    """This is a test to read the addition calculation results"""
    # Arrange
    filename = 'addition.csv'
    path = 'tests/test_data'
    full_path = path + '/' + filename
    # Act
    df = Read.DataFrameFromCSVFile(full_path)
    # Assert
    assert type(df) is pandas.DataFrame
    print(df)