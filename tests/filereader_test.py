"""Testing File reader Using Pandas"""

from calc.utils.filereader import PandasFileReader

def test_filereader():
    """File reader"""

def test_filetype_validate(addition_file_fixture):
    """Validating file type"""
    #Arrange
    file_name = "addition.csv"
    #Act
    df_test_data = PandasFileReader(file_name).read_file()
    #Assert
    assert df_test_data is not None
