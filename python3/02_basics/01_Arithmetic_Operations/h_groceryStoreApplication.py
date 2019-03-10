#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

"""

costOfApple = 12
costOfMango = 5
# NOTE: raw_input() takes every input as a string type only
#       raw_input() in python 2 is input() in python 3

# secure coding - OWASP
# quantityOfApples = input('quantityOfApples=')
# quantityOfMangos = input('quantityOfMangos=')

quantityOfApples = int(input('quantityOfApples='))
quantityOfMangos = float(input('quantityOfMangos='))

print("type(quantityOfApples) = ", type(quantityOfApples))
print('quantityOfApples:', quantityOfApples)

TotalCost = (costOfApple * quantityOfApples) + (costOfMango * quantityOfMangos)
print("Total Cost = ", TotalCost)






