"""log writer"""
import logging

# logging
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

fh = logging.FileHandler('file.log')

fh.setFormatter(f)

logger.addHandler(fh)

logging.info("log writer initiate")


def output_data(filename, value_1, operation, value_2, result):
    """Output file writing"""

    logger.debug(f'writing data to {filename}..')
    with open('file.log', 'a') as appendFile:
        appendFile.write(
            f'Filename:{filename} - Value_1:{value_1}, '
            f'Operation:{operation}, Value_2:{value_2} - Result:{result}\n')
    return appendFile
logger.info(f"Log Writer process successfully completed")
