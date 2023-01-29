#!/usr/bin/env python

"""
python-colorlog example
"""
import logging
import sys

import pip

try:
    from colorlog import ColoredFormatter
except ImportError as ex:
    print(ex)
    print("Installing that module")
    pip.main(["install", str(ex).split("No module named ")[1]])
    from colorlog import ColoredFormatter


def setup_logger():
    """
    Returns a logger with a default ColoredFormatter.
    """
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red",
        },
    )

    logger = logging.getLogger("example")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


def main():
    logger = setup_logger()

    logger.debug("a debug message")
    logger.info("an info message")
    logger.warning("a warning message")
    logger.error("an error message")
    logger.critical("a critical message")


if __name__ == "__main__":
    main()
