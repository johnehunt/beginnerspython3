import logging
import printer_lib

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    logger.warning('This is a warning!')
    logger.info('This is just for information')
    logger.debug('This is to help with debugging')
    logger.error('This should be used with something unexpected')
    logger.critical('Something serious')

    logger.warning('%s is set to %d', 'count', 42)

    try:
        x = 1 / 0
        print(x)
    except:
        logger.exception('an exception message')

    printer_lib.do_something()

    pr = printer_lib.Printer()
    pr.print_something()


if __name__ == '__main__':
    main()
