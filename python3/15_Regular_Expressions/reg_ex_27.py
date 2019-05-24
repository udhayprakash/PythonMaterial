#!/usr/bin/python
"""
purpose: regular expression  demo 

Ex: email ids
"""

import re 


p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue Lorries and red Busses'))
print(p.subn('colour', 'blue Lorries and red Busses'))

