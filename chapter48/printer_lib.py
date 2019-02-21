import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.warning('Well how about that then!')

def do_something():
    logger.info('do something!')


class Printer:

    def print_something(self):
        logger.info('print it')
        print('something')