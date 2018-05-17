#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

"""

# costOfApple = 12
# costOfMango = 5
costOfApple = input('Enter the cost of Each Apple:')  
costOfMango = input('Enter the cost of Each Mango:')

print "type(costOfApple) = ", type(costOfApple)

quantityOfApples = 3
quantityOfMangos = 7

TotalCost = (costOfApple * quantityOfApples) + (costOfMango * quantityOfMangos)
print "Total Cost = ", TotalCost
# NOTE: Due to security issues, input() is discarded