import logging
import logging.config
from config_1 import log_file

def main():
    x=log_file()
    # print(x)
    logging.config.dictConfig(x)
    logger = logging.getLogger("exampleApp")

    logger.info("program started")
    print("on the way")
    logger.info("program ended")

    # logging.debug('This is a debug message')
    # logging.info('This is an info message')
    # logging.warning('This is a warning message')
    # logging.error('This is an error message')
    # logging.critical('This is a critical message')

if __name__ == "__main__":
    main()