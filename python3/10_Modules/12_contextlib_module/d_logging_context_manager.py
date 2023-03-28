import logging
from contextlib import contextmanager


@contextmanager
def log(level):
    logger = logging.getLogger()
    current_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(current_level)


def some_function():
    logging.debug("Some debug level information...")
    logging.error("Serious error...")
    logging.warning("Some warning message...")


with log(logging.DEBUG):
    some_function()

# DEBUG:root:Some debug level information...
# ERROR:root:Serious error...
# WARNING:root:Some warning message...
