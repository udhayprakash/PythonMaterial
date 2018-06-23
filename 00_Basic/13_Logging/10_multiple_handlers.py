import logging 
import sys
import os

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)
errfile = logging.FileHandler(
    filename=os.path.splitext(__file__)[0] + '.log'
    )

fmt = logging.Formatter('%(levelname)s %(name)s %(message)s')
stdout.setFormatter(fmt)
errfile.setFormatter(fmt)

errfile.setLevel('ERROR')
logger.setLevel('DEBUG')

logger.addHandler(stdout)
logger.addHandler(errfile)

logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
