# Formatting examples

import logging

# Several different formatting options - try uncommenting different ones
# logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s[%(levelname)s] %(funcName)s: %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logger = logging.getLogger(__name__)


def do_something():
    logger.debug('This is to help with debugging')
    logger.info('This is just for information')
    logger.warning('This is a warning!')
    logger.error('This should be used with something unexpected')
    logger.critical('Something serious')


do_something()
