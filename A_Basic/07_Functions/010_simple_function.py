#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with variable keyword arguments
"""

# Function Definition
def hello(*given, **feed_in):
    print "\ntype(given)  ",  type(given)
    print "type(feed_in) ",  type(feed_in)

    print "given   "+ str(given)
    print "feed_in "+ str(feed_in)
    print '-'*20

# Function Call 
hello()            # 0 inputs
hello('HARI')      # 1 input
hello(name='HARI')      # 1 input

hello(language='Python')
hello(years=365)

hello(country='India', age=75)

hello(212.34, 'India', age=75, number=34, mystring='sdas', larger_number=342432)