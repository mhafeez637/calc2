"""CSV Addition Test"""
import os
import logging
import pandas as pd
import main as log
from calc.calculations.addition import Addition

# Directory Path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def test_calculation_addition():
    # Arrange
    filename = "test_data/addition.csv"
    path = os.path.join(BASE_DIR, filename)
    df = pd.read_csv(path)

    print("Scan CSV Addition files in folder")
    # Act
    for x, row in df.iterrows():
        xyz = (row.value_1, row.value_2)
        addition = Addition.create(xyz)
        addition_result = df["result"][x]
        log.Write_data(filename, row.value_1, "+", row.value_2, addition_result)
        logging.debug("Addition Result")

    # Assert
    assert addition.get_result() == addition_result

    print("Addition CSV file and data has successfully verified")