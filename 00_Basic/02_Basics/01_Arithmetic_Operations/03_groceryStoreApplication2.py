#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

"""

#costOfApple = 12
#costOfMango = 5
# NOTE: raw_input() takes every input as a string type only
costOfApple = float(raw_input('Enter the cost of Each Apple:'))   # input()
costOfMango = float(raw_input('Enter the cost of Each Mango:'))

print "type(costOfApple) = ", type(costOfApple)

quantityOfApples = 3
quantityOfMangos = 7

TotalCost = (costOfApple * quantityOfApples) + (costOfMango * quantityOfMangos)
print "Total Cost = ", TotalCost
