#!/usr/bin/python

def eo(num):
  ''' fun for even odd numbers '''
  if num % 2 == 0:
    print('even')
  else:
    print('odd') 

import pdb
pdb.set_trace()
for i in range(100):
  print("The number1 is %s" %(i))
  print("The number2 is %s" %(i))
  print("The number3 is %s" %(i))
  print("The number4 is %s" %(i))
  print("The number5 is %s" %(i))
  eo(i)

