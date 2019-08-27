#!/usr/bin/python
"""
Purpose; multiple loggers 
        - FileHandler 
        - StreamHandler
"""
import logging 
import sys
import os


fmt = logging.Formatter('%(asctime)s %(levelname)8s %(name)s %(message)s')

stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setFormatter(fmt)

errfile = logging.FileHandler(
    filename=os.path.splitext(__file__)[0] + '.log'
    )
errfile.setFormatter(fmt)
errfile.setLevel('ERROR')


logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

logger.addHandler(stdout)
logger.addHandler(errfile)

logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
