#!/usr/bin/python
# shebang line

'''
Purpose: This is a demonstration script
'''
print 'hello world!'
print "hello world!"

# python is a dynamic typed language
a = 12
b = 34

c = a + b
print 'c =', c   # , logic separator

type(a)  # until we place print statement, nothing from the script will be
         # displayed on console

print 'type(a)=', type(a)

a = False
print 'type(a)=', type(a)


a = 'False'
print 'type(a)=', type(a)

a = '12'
print 'type(a)=', type(a)
