#!/usr/bin/python
# second.py

import logging

logging.basicConfig(
    filename='06_logging.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG)

# diskspace=90
choice = 'Y'
while choice.upper() == 'Y':
    diskspace = int(raw_input('Enter the diskspace, in integers : '))
    if diskspace == 0:
        logging.debug('You have hit the warning message - disspace %d', diskspace)
    elif diskspace > 20 and diskspace < 50:
        logging.info('You have hit the warning message - disspace %d', diskspace)
    elif diskspace > 50 and diskspace < 85:
        logging.warning('You have hit the warning message - disspace %d', diskspace)
    elif diskspace > 85 and diskspace < 91:
        logging.warning('You have hit the warning message - disspace %d', diskspace)
    else:
        logging.critical('You have hit the warning message - disspace %d', diskspace)

    choice = raw_input('Do you want to retry: Y or N: ')
