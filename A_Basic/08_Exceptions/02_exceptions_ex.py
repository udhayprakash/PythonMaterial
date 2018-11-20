#!/usr/bin/python
# SyntaxError cant be handled 
try:
    result ='1' / 0 + bat
    print 'result=', result
except ZeroDivisionError as ex:
    print 'ZeroDivisionError error is ', ex
    print 'error is ', str(ex)
    print 'error is ', repr(ex)
except NameError as ex1:
    print 'NameError error is ', ex1
    print 'error is ', str(ex1)
    print 'error is ', repr(ex1)
except TypeError as ex1:
    print 'TypeError error is ', ex1
    print 'error is ', str(ex1)
    print 'error is ', repr(ex1)
except Exception as ex2:
    print 'Exception - error is ', ex2
    print 'error is ', str(ex2)
    print 'error is ', repr(ex2)