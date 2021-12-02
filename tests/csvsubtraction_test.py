"""CSV Subtraction Test"""

import os
import logging
import pandas as pd
import log.logs as log
from calc.calculations.subtraction import Subtraction

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_calculation_subtraction():
    # Arrange
    filename = "test_data/subtraction.csv"

    path = os.path.join(BASE_DIR, filename)

    df = pd.read_csv(path)

    print("Scan CSV Subtraction files in folder")
    # Act
    for x, row in df.iterrows():
        xyz = (row.value_1, row.value_2)
        subtraction = Subtraction.create(xyz)
        subtraction_result = df["result"][x]
        log.Write_data(filename, row.value_1, "+", row.value_2, subtraction_result)
        logging.debug("Subtraction Result")

    # Assert
    assert subtraction.get_result() == subtraction_result

    print("Subtraction CSV file and data has successfully verified")