#!/usr/bin/python
"""
when no error - try - else  - finally
when error    - try - except - finally
"""
try:
    result = 1 / 10
except Exception as ex:
    print 'error is ', ex
    print 'error is ', str(ex)
    print 'error is ', repr(ex)
else:
    print 'result=', result
finally:
    print "finally"

print "outside "