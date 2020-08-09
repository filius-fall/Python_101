import logging
logging.basicConfig(filename="logs/sample.log", level=logging.INFO)
log = logging.getLogger("ex")
try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")