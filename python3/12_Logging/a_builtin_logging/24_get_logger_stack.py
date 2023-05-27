import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def my_function():
    filename, line_no, co_name, sinfo = logger.findCaller()

    # Log a message with the caller's frame information
    logger.info(f"Function called from {filename}, line {line_no}")


def another_function():
    filename, line_no, co_name, sinfo = logger.findCaller()

    # Log a message with the caller's frame information
    logger.info(f"Function called from {filename}, line {line_no}")


def main():
    logger.info("Application started")
    my_function()
    another_function()
    logger.info("Application finished")


if __name__ == "__main__":
    main()
