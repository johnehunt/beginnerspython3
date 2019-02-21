# Programmatically setting the handler

import logging

# Empty basic config turns off default console handler
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler which logs to the specified file
file_handler = logging.FileHandler('detailed.log')

# Create formatter for the file_handler
formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# 'application' code
def do_something():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


logger.info('Starting')
do_something()
logger.info('Done')

