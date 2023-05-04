from loguru import logger

child_logger = logger.bind(user="GudoVanRussom")

child_logger.info("This message will include a logger name")


# Disabling logging for a specific module
logger.disable("__main__")

logger.info("This message will not be logged")

# Enabling logging for a specific module
logger.enable("__main__")

logger.info("This message will be logged")
