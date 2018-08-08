#!/usr/bin/python
"""
Purpose: Functions Demo

   Scope - Global and local 
"""
global num1
num1 = 121  # immutable object 


def computation():
    global num1
    print 'num1', num1
    num1 = 999
    print 'num1', num1

computation()
print 'outside --- num1', num1