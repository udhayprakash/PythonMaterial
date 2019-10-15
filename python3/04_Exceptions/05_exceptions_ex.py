#!/usr/bin/python

# raise ValueError('This is my ValueError')
raise TypeError('This is my TYpeError')


try:
    raise ValueError('This is my ValueError')
    # raise Exception('This is my error')
except ValueError as ex2:
    print('ValueError error is ', repr(ex2))
except Exception as ex2:
    print('Exception error is ', repr(ex2))
else:
    print('no exceptions')
finally:
    print('finally will be executed in all the cases')

# when no exception -> try -> else -> finally
# when  exception  -> try -> except -> finally
