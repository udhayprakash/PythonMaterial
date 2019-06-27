import logging, logging.handlers, atexit, sys

filename = 'mylogfile.txt'
logLevel = logging.DEBUG

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
streamhandler = logging.StreamHandler(sys.stderr)
streamhandler.setLevel(logLevel)
streamhandler.setFormatter(formatter)
memoryhandler = logging.handlers.MemoryHandler(
    capacity=1024*100,
    flushLevel=logging.ERROR,
    target=streamhandler
)

filehandler = logging.FileHandler(filename)
filehandler.setLevel(logLevel)
filehandler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logLevel)
logger.addHandler(memoryhandler)
logger.addHandler(filehandler)
def flush():
    memoryhandler.flush()
atexit.register(flush)
logging.debug("Logger has Initialized")
sys.stderr.write("I'd like this printed on the console first\n")