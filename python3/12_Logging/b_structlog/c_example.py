import logging
import structlog
from structlog.stdlib import LoggerFactory

logging.basicConfig()
structlog.configure(logger_factory=LoggerFactory())  
log = structlog.get_logger()
log.warning("it works!", difficulty="easy")  