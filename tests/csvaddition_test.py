"""CSV Addition Test"""
import os
import logging
import pandas as pd
from tests import log
from calc.calculations.addition import Addition

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# pylint: disable=unsubscriptable-object
def test_calculation_addition():
    """ testing addition csv file"""
    # Arrange
    filename = "test_data/addition.csv"
    path = os.path.join(BASE_DIR, filename)
    data_frame = pd.read_csv(path)

    print("Scan CSV Addition files in folder")
    # Act
    for index, row in data_frame.iterrows():
        xyz = (row.value_1, row.value_2)
        addition = Addition.create(xyz)
        addition_result = data_frame["result"][index]
        log.output_data(filename, row.value_1, "+", row.value_2, addition_result)
        logging.debug("Addition Result")

    # Assert
    assert addition.get_result() == addition_result

    print("Addition CSV file and data has successfully verified")
