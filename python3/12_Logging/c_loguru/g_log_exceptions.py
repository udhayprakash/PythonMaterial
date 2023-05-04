import sys

from loguru import logger

try:
    raise ValueError("Invalid value")
except ValueError:
    logger.exception("An error occurred")
    logger.exception(
        "An exception occurred", extra={"context": "some context information"}
    )


# custom exception handler


def exception_handler(exception):
    logger.error(f"Exception: {exception}")


# logger.add(sys.stderr, exception_handler=exception_handler)

# try:
#     # some code that may raise an exception
#     1/0
# except Exception as e:
#     logger.exception(e)
