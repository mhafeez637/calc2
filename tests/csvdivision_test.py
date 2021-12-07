"""CSV Division Test"""

import os
import logging
import pytest
import pandas as pd
import log
from calc.calculations.division import Division

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# pylint: disable=unsubscriptable-object
def test_calculation_division():
    """ testing division csv file"""

    # Arrange
    filename = "test_data/division.csv"
    path = os.path.join(BASE_DIR, filename)
    data_frame = pd.read_csv(path)

    print("Scan CSV Division files in folder")
    # Act
    for index, row in data_frame.iterrows():
        xyz = (row.value_1, row.value_2)
        division = Division.create(xyz)
        division_result = data_frame["result"][index]
        log.output_data(filename, row.value_1, "+", row.value_2, division_result, index)
        logging.debug("Division Result")
    try:
        # Assert
        assert division.get_result() == division_result
    except ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            assert division.get_result() is True

    print("Division CSV file and data has successfully verified")
