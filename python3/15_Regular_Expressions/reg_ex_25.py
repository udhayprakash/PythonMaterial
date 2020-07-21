#!/usr/bin/python
"""
purpose: regular expression  demo 

Ex: email ids
"""

import re

re.split('[.]', '244.255.190.23')
re.split('.', '244.255.190.23')
re.split(r'\.', '244.255.190.23')

r'''
>>> re.split('\.', '244.255.190.23')
['244', '255', '190', '23']
>>> re.split('\.', '244.255.190.23', 0)
['244', '255', '190', '23']
>>> re.split('\.', '244.255.190.23', 1)
['244', '255.190.23']
>>> re.split('\.', '244.255.190.23', 2)
['244', '255', '190.23']
>>> re.split('\.', '244.255.190.23', 3)
['244', '255', '190', '23']
>>> re.split('\.', '244.255.190.23', 6)
['244', '255', '190', '23']
>>>
'''