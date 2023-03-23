"""
Purpose: module_scope_fixture
    - This fixture will run once per test module.
    - It can be used for setup that needs to be done once for all the tests in a module.
    - For example, you might use this to set up a logger that will be used across multiple tests.
"""
import logging

import pytest


@pytest.fixture(scope="module")
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    yield logger
    logger.removeHandler(handler)


class TestLogging:
    def test_log_message(self, logger):
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
