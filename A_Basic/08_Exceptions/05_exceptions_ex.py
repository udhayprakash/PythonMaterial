#!/usr/bin/python

try:
    raise Exception('This is my error')
except Exception as ex2:
    print 'error is ', ex2
    print 'error is ', str(ex2)
    print 'error is ', repr(ex2)
else:
    print 'no exceptions'
finally:
    print 'finally will be executed in all the cases'

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
