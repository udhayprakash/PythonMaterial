import logging
import logging.config

GLOBAL_STUFF = 1


class ContextFilter(logging.Filter):
    def filter(self, record):
        global GLOBAL_STUFF
        GLOBAL_STUFF += 1
        record.global_data = GLOBAL_STUFF
        return True


handler = logging.StreamHandler()
handler.formatter = logging.Formatter("%(global_data)s %(message)s")
handler.addFilter(ContextFilter())
logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.error("Hi1")
logger.error("Hi2")
