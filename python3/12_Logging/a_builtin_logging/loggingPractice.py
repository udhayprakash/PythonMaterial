import logging
import os
import platform

if platform.platform().startswith("Windows"):
    loggingFile = os.path.join(
        os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "test.log"
    )
else:
    loggingFile = os.path.join(os.getenv("HOME"), "test.log")

print("Logging to ", loggingFile)

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(process)-5d] [%(funcName)-27s] [%(levelname)-8s] %(message)s",
    filename=loggingFile,
    filemode="w",
)

logging.debug("=" * 100)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
