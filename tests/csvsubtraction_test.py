"""CSV Subtraction Test"""
import os
import logging
import pandas as pd
import log
from calc.calculations.subtraction import Subtraction

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# pylint: disable=unsubscriptable-object
def test_calculation_subtraction():
    """ testing Subtraction csv file"""
    # Arrange
    filename = "test_data/subtraction.csv"

    path = os.path.join(BASE_DIR, filename)

    data_frame = pd.read_csv(path)

    print("Scan CSV Subtraction files in folder")
    # Act
    for index, row in data_frame.iterrows():
        xyz = (row.value_1, row.value_2)
        subtraction = Subtraction.create(xyz)
        subtraction_result = data_frame["result"][index]
        log.output_data(filename, row.value_1, "+", row.value_2, subtraction_result, index)
        logging.debug("Subtraction Result")

        data_frame.to_csv(r'tests/test_data_process/Subtraction_processed.csv', encoding='utf-8', index=True
        )

    # Assert
    assert subtraction.get_result() == subtraction_result

    print("Subtraction CSV file and data has successfully verified")

