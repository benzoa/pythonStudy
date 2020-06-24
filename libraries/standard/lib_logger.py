import logging as log
import mylib
import logging.handlers


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


def use_logger():
    logger = log.getLogger('mylogger')
    logger.setLevel(log.DEBUG)
    
    fmt = '[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s] > %(message)s'
    formatter = log.Formatter(fmt=fmt, datefmt='%y%m%d %H:%M:%S')

    filename = './example.log'
    
    file_max_byte = 1024 * 1024 * 10 # 10MB
    file_handler = logging.handlers.RotatingFileHandler(filename, maxBytes=file_max_byte, backupCount=20)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = log.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    logger.debug('This message should appear on the console')
    logger.info('So should this')
    logger.warning('And this, too')  


if __name__ == '__main__':
    # simple_log()
    # formatted_log()
    use_logger()
