# Filter example

import logging


# Define a filter subclass
class MyFilter(logging.Filter):

    def filter(self, record):
        if 'John' in record.msg:
            return False
        else:
            return True


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

# Set up the filter on the logger
logger = logging.getLogger(__name__)
logger.addFilter(MyFilter())

# Application code with logging
logger.debug('This is to help with debugging')
logger.info('This is information on John')
