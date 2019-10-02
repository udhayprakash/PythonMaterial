#!/usr/bin/python

try:
    result = 11 / '0' + bat
    print('result=', result)
except ZeroDivisionError as ex:
    print('ZeroDivisionError - error is ', repr(ex))
except NameError as ex1:
    print('NameError - error is ', repr(ex1))
except Exception as ex2:
    print('Exception - error is ', repr(ex2))
else:
    print('no exceptions')
finally:
    print('finally will be executed in all the cases')

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
