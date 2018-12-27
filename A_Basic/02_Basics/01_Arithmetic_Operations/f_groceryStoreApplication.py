#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

"""

costOfApple = 12
costOfMango = 5

quantityOfApples = input('Enter quantity of Apples:')
print "type(quantityOfApples) = ", type(quantityOfApples)

quantityOfMangos = input('quantityOfMangos=')

TotalCost = ((costOfApple * quantityOfApples)
             + (costOfMango * quantityOfMangos))
print "Total Cost = ", TotalCost
# NOTE: Due to security issues, input() is discarded

"""
#python 04_groceryStoreApplication.1.py
quantityOfApples=2
quantityOfMangos=4
type(quantityOfApples) =  <type 'int'>
Total Cost =  44

#python 04_groceryStoreApplication.1.py
quantityOfApples=2.5
quantityOfMangos=4.66666
type(quantityOfApples) =  <type 'float'>
Total Cost =  53.3333

#python 04_groceryStoreApplication.1.py
quantityOfApples='2'
quantityOfMangos='4'
type(quantityOfApples) =  <type 'str'>
Total Cost =  22222222222244444

#python 04_groceryStoreApplication.1.py
quantityOfApples="2"
quantityOfMangos="4"
type(quantityOfApples) =  <type 'str'>
Total Cost =  22222222222244444

#python 04_groceryStoreApplication.1.py
quantityOfApples=True
quantityOfMangos=False
type(quantityOfApples) =  <type 'bool'>
Total Cost =  12
"""
