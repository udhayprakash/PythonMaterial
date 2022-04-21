#!/usr/bin/python
# buggyFifth.py
def eo(num):
  ''' fun for even odd numbers '''
  if num % 2 == 0:
    return 'even'
  else:
    return 'odd'

import pdb;pdb.set_trace()
print eo(2)
print eo(3)
print eo.func_doc
