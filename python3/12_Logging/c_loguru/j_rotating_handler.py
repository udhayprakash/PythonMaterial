# from loguru import logger
# from loguru.handlers import RotatingFile

# handler = RotatingFile("file.log", max_size="1 MB", backup_count=3)
# logger.add(handler)

# logger.info("This message will be logged to a rotating file")


# # Timed Rotating Handler
# from loguru.handlers import TimedRotatingFile

# handler = TimedRotatingFile("file.log", when="midnight")
# logger.add(handler)

# logger.info("This message will be logged to a timed rotating file")


# from loguru import logger
# from loguru._file_sink import TimedRotatingFileSink

# logger.add(TimedRotatingFileSink("logs/myapp.log", when="midnight", interval=1, backup_count=7))

# logger.info("This message will be logged to a timed rotating file")

from loguru import logger
from loguru._file_sink import WatchedFileSink

logger.add(WatchedFileSink("logs/myapp.log"))

logger.info("This message will be logged to a watched file")
