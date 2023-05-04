import sys

from loguru import logger

logger.add(sys.stderr, format="{extra[user]} - {message}")

logger.bind(user="johndoe").info("This message will include the user context")
