from loguru import logger

try:
    raise ValueError("Invalid value")
except ValueError:
    logger.exception("An error occurred")
