from loguru import logger

# def my_function():
#     logger.info("Entering my_function")
#     raise Exception()
#     logger.info("Exiting my_function")

# my_function()


@logger.catch
def my_function2():
    logger.info("Entering my_function")
    raise Exception()
    logger.info("Exiting my_function")


my_function2()