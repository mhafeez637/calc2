"""log writer"""
import logging

# logging
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(recored_number)s %(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

filehandling = logging.FileHandler('file.log')

filehandling.setFormatter(formatter)

logger.addHandler(filehandling)

logging.info("log writer initiate")


def output_data(filename, value_1, operation, value_2, result, log_counter):
    """Output file writing"""
    log_counter = log_counter + 1
    logger.debug(f'writing data to {filename}..')
    with open('file.log', 'a') as append_file:
        append_file.write(
            f'Filename:{filename} -Record Number:{log_counter} - Value1:{value_1}, Operation:{operation}, '
            f'Value2:{value_2} - Result:{result}\n')
    return append_file


logger.info(f"Log Writer process successfully completed")
