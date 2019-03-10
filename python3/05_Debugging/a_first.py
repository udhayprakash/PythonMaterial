#!/usr/bin/python
# first.py
import pdb

version = '3.0'


def hello():
    ''' this is just for printing hello '''
    print "hello today is modules class"


def add(a=1, b=2):
    ''' this is an addition program '''
    sum = a + b
    return sum


pdb.set_trace()
if __name__ == '__main__':
    hello()
    sum = add()
    sum1 = add(5, 6)
    print sum1
    print sum
    print version
else:
    print "Hello this has to be part of my modules"
