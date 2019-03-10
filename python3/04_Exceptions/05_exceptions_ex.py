#!/usr/bin/python

# raise NameError('This is my NameError')

try:
    # raise ValueError('This is my ValueError')
    raise Exception('This is my error')
except ValueError as ex2:
    print('ValueError error is ', ex2)
    print('error is ', repr(ex2))
except Exception as ex2:
    print('Exception error is ', ex2)
    print('error is ', repr(ex2))
else:
    print('no exceptions')
finally:
    print('finally will be executed in all the cases')

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
