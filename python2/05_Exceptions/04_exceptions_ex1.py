#!/usr/bin/python

try:
    result = bat + 1 / 0
    print 'result=', result
except (ZeroDivisionError, NameError) as ex2:
    print 'error is ', ex2
    print 'error is ', str(ex2)
    print 'error is ', repr(ex2)
except Exception as ex2:
    print 'Exception error is ', ex2
    print 'error is ', str(ex2)
    print 'error is ', repr(ex2)
else:
    print 'no exceptions'
finally:
    print 'finally will be executed in all the cases'

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
