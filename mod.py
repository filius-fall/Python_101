import logging

module_logger=logging.getLogger("module_logger")
def add(x,y):
    # logging.info("added %s and %s to get %s" %(x,y,x+y))
    add_logger = logging.getLogger("add_logger")
    add_logger.info("added %s and %s to get %s" %(x,y,x+y))

    return x+y