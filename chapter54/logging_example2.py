# Setting the default format for log message output

import logging

logging.basicConfig(format='%(asctime)s - %(message)s')

logger = logging.getLogger()

logger.debug('This is to help with debugging')
logger.error('This should be used with something unexpected')
logger.critical('Something serious')

