#!/usr/bin/python
"""
Problem Statement:
	Assume that price is an integer variable whose value is the price (in US currency) in cents of an item.
	Write a statement that prints the value of price in the form "X dollars and Y cents" on a line by itself.
	So, if the value of price was 4321, your code would print "43 dollars and 21 cents".
	Ex: If the value was 501 it would print "5 dollars and 1 cents".
	Ex: If the value was 99 your code would print "0 dollars and 99 cents".
"""


def formatted_result(price):
    return "%d dollor(s) and %d cent(s)" % (price / 100, price % 100)
    # default return is None


print(formatted_result(4321))  # '43 dollor(s) and 21 cent(s)'

print(formatted_result(501))  # '5 dollor(s) and 1 cent(s)'
