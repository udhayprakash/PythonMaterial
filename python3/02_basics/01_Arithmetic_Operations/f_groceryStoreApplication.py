#!/usr/bin/python
"""
Purpose: Grocery Store Demonstration

Products: Apples and Mangos

Python 2 
    input() 
    raw_input()


python 3 
    input()  --- raw_input() in python 2 is renamed as input() here
"""

cost_of_apple = 12
cost_of_mango = 5


qty_of_apples = float(input('HOw many apples you need(in numbers):'))
print('qty_of_apples = ', qty_of_apples, type(qty_of_apples))

# type convertors int(), float()

qty_of_mangos = int(input('HOw many mangos you need(in numbers):'))
print('qty_of_mangos = ', qty_of_mangos)

total_cost = cost_of_apple * qty_of_apples + \
                cost_of_mango * qty_of_mangos

print('total_cost = ', total_cost)
















"""
Python 2 - input()
# NOTE: Due to security issues, input() is discarded

    #python 04_groceryStoreApplication.1.py
    quantity_of_apples=2
    quantity_of_mangos=4
    type(quantity_of_apples) =  <type 'int'>
    Total Cost =  44

    #python 04_groceryStoreApplication.1.py
    quantity_of_apples=2.5
    quantity_of_mangos=4.66666
    type(quantity_of_apples) =  <type 'float'>
    Total Cost =  53.3333

    #python 04_groceryStoreApplication.1.py
    quantity_of_apples='2'
    quantity_of_mangos='4'
    type(quantity_of_apples) =  <type 'str'>
    Total Cost =  22222222222244444

    #python 04_groceryStoreApplication.1.py
    quantity_of_apples="2"
    quantity_of_mangos="4"
    type(quantity_of_apples) =  <type 'str'>
    Total Cost =  22222222222244444

    #python 04_groceryStoreApplication.1.py
    quantity_of_apples=True
    quantity_of_mangos=False
    type(quantity_of_apples) =  <type 'bool'>
    Total Cost =  12
"""
