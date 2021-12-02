"""CSV Division Test"""
import os
import pytest
import logging
import pandas as pd
import log.logs as log
from calc.calculations.division import Division

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_calculation_division():
    # Arrange
    filename = "test_data/division.csv"
    path = os.path.join(BASE_DIR, filename)
    df = pd.read_csv(path)

    print("Scan CSV Division files in folder")
    # Act
    for x, row in df.iterrows():
        xyz = (row.value_1, row.value_2)
        division = Division.create(xyz)
        division_result = df["result"][x]
        log.Write_data(filename, row.value_1, "+", row.value_2, division_result)
        logging.debug("Division Result")
    try:
        # Assert
        assert division.get_result() == division_result
    except ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            assert division.get_result() is True

    print("Division CSV file and data has successfully verified")