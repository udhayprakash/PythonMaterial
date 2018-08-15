#!/usr/bin/python

try:
    result = 1 / 0
    print 'result=', result
except Exception as ex:
    print 'error is ', ex
    print 'error is ', str(ex)
    print 'error is ', repr(ex)