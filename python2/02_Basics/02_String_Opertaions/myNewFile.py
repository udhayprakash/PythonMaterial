#!/usr/bin/python

'''
myNewFile.py
Purpose:  Demonstration
'''

# This is new program
# This is another line
# This is another line
# This is another line


#either single, single or double quotes, can be used for strings

costOfMango = 12  # cost_of_mango
print "cost Of Each Mango is ", costOfMango

costOfApple = 40
print "cost Of Each Apple is ", costOfApple

# what is the cost of dozen apples and two dozens of mangos

dozen = 12

TotalCost = dozen* costOfApple + 2*dozen* costOfMango

print "Total cost is ", TotalCost

# print is a statement in python 2, and is a function call in python 3


# now, python 2 is supporting both

print "Hello World!"       # print is a statement  -- works in python 2.x only
print("Hello World!")      # print is a function   -- works in both python 2.x and 3.x


# by default, print will lead to display in next line

print "This is",   # , after print will suppress the next line
                   # but, a space will result
print "python class"

# PEP 8 recommends to use only print statement or function call throughtout the project

# ; semicolon operator
# It is used as a statement separator.


name = 'yash'
print 'My name is ', name

name = 'yash'; print 'My name is ', name

print "who's name is ", name, '?'


