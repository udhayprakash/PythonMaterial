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
cost_of_apple = 23
cost_of_mango = 56

qty_of_apples = int(input('Enter qty. of apples(in num):'))
print('qty_of_apples', qty_of_apples, type(qty_of_apples))

qty_of_mangos = float(input('Enter qty. of mangos(in num):'))

# int(), float(), str()

sp_of_apples = cost_of_apple * qty_of_apples
print('sp_of_apples:', sp_of_apples)

# Assignment                100
    # discount of 10 %       90

    # GST of 7.5 %  







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
