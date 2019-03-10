#!/usr/bin/python

try:
    result = 1 / 0 + bat
    print 'result=', result
except Exception as ex2:
    print 'umbrella exception'
    print 'error is ', str(ex2)
    print 'error is ', repr(ex2)
except ZeroDivisionError as ex:
    print 'dont divide by zero'
    print 'error is ', str(ex)
    print 'error is ', repr(ex)
except NameError as ex1:
    print 'define variable before usage'
    print 'error is ', str(ex1)
    print 'error is ', repr(ex1)
else:
    print 'no exceptions'
finally:
    print 'finally will be executed in all the cases'

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
