from structlog import configure, get_logger
from structlog.stdlib import LoggerFactory

configure(logger_factory=LoggerFactory())
log = get_logger()
log.critical("this is too easy!")
