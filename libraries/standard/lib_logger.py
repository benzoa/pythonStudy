import logging as log
import mylib


def simple_log():
    log.basicConfig(filename='example.log', filemode='a', level=log.DEBUG)
    log.debug('This message should go to the log file')
    log.info('So should this')
    log.warning('And this, too')


def formatted_log():
    log.basicConfig(format='[%(levelname)s] %(asctime)s, %(message)s', datefmt='%Y.%m.%d %H:%M:%S', level=log.DEBUG)
    log.debug('This message should appear on the console')
    log.info('So should this')
    log.warning('And this, too')

    log.warning('%s before you %s', 'Look', 'leap!')

    log.info('Started')
    mylib.do_something()
    log.info('Finished')


if __name__ == '__main__':
    # simple_log()
    
    formatted_log()
