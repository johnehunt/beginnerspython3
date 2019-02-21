# Example of logging to a file

import logging

# Sets a file handler ont he root logger to
# save log messages to the example.log file
logging.basicConfig(filename='example.log',level=logging.DEBUG)

# If no handler is explicitly set on the name logger
# it will delegate the messages to the parent logger to handle
logger = logging.getLogger(__name__)

logger.debug('This is to help with debugging')
logger.info('This is just for information')
logger.warning('This is a warning!')
logger.error('This should be used with something unexpected')
logger.critical('Something serious')