# Multiple Handlers and formatters
import logging

# Set up the default root logger to do nothing
logging.basicConfig(handlers=[logging.NullHandler()])

# Obtain the module level logger and set level to DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('detailed.log')

# Create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Create formatter for the file handler
fh_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s',
                                 datefmt='%m-%d-%Y %I:%M:%S %p')
file_handler.setFormatter(fh_formatter)

# Create formatter for the console handler
console_formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Add the handlers to logger
logger.addHandler(console_handler)
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
