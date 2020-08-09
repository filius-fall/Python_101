import logging
import logging.config
from config_1 import log_file

def main(x):
    
    logging.config.dictConfig(x)
    logger=logging.getLogger("exampleapp")

    logger.info("program started")
    print("on the way")
    logger.info("program ended")

if __name__ == "__main__":
    config_file=log_file()
    main(config_file)