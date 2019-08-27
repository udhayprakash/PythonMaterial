#!/usr/bin/python
import logging
from pprint import pformat

data = [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
 (2,
  {'e': 'E',
   'f': 'F',
   'g': 'G',
   'h': 'H',
   'i': 'I',
   'j': 'J',
   'k': 'K',
   'l': 'L'})]

logging.basicConfig(level=logging.DEBUG,
					format='%(levelname)-8s %(message)s',
				)

logging.debug('Logging pformatted data')
logging.debug(data)

formatted = pformat(data)
for line in formatted.splitlines():
	logging.debug(line.rstrip())

