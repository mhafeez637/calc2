"""CSV Multiplication Test"""
import os
import logging
import pandas as pd
import log
from calc.calculations.multiplication import Multiplication

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# pylint: disable=unsubscriptable-object
def test_calculation_multiplication():
    """ testing Multiplication csv file"""
    # Arrange
    filename = "test_data/multiply.csv"

    path = os.path.join(BASE_DIR, filename)

    data_frame = pd.read_csv(path)

    print("Scan CSV Multiplication files in folder")
    # Act
    for index, row in data_frame.iterrows():
        xyz = (row.value_1, row.value_2)
        multiplication = Multiplication.create(xyz)
        multiplication_result = data_frame["result"][index]
        log.output_data(filename, row.value_1, "+", row.value_2, multiplication_result, index)
        logging.debug("Multiplication Result")

    data_frame.to_csv(r'tests/test_data_process/Multiplication_processed.csv', encoding='utf-8', index=True)

    # Assert
    assert multiplication.get_result() == multiplication_result

    print("Multiplication CSV file and data has successfully verified")
