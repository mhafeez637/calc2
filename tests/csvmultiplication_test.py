"""CSV Multiplication Test"""

import os
import logging
import pandas as pd
import log.logs as log
from calc.calculations.multiplication import Multiplication

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_calculation_multiplication():
    # Arrange
    filename = "test_data/multiply.csv"

    path = os.path.join(BASE_DIR, filename)

    df = pd.read_csv(path)

    print("Scan CSV Multiplication files in folder")
    # Act
    for x, row in df.iterrows():
        xyz = (row.value_1, row.value_2)
        multiplication = Multiplication.create(xyz)
        multiplication_result = df["result"][x]
        log.Write_data(filename, row.value_1, "+", row.value_2, multiplication_result)
        logging.debug("Multiplication Result")

    # Assert
    assert multiplication.get_result() == multiplication_result

    print("Multiplication CSV file and data has successfully verified")