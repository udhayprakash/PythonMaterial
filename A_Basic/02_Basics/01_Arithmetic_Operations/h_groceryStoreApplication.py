#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

"""

costOfApple = 12
costOfMango = 5
# NOTE: raw_input() takes every input as a string type only
#       raw_input() in python 2 is input() in python 3 

# quantityOfApples = raw_input('quantityOfApples=')
# quantityOfMangos = raw_input('quantityOfMangos=')

quantityOfApples = float(raw_input('quantityOfApples='))
quantityOfMangos = float(raw_input('quantityOfMangos='))
print "type(quantityOfApples) = ", type(quantityOfApples)
print 'quantityOfApples:', quantityOfApples

TotalCost = (costOfApple * quantityOfApples) + (costOfMango * quantityOfMangos)
print "Total Cost = ", TotalCost






