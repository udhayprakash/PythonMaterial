#!/usr/bin/python
"""
Purpose: Grocery Store

    Item       cost         
    ------------------------
    rice        52/kg       
    wheat       34/kg       

input() -> to get value in run-time
        -> will give any input as string only
"""

# cost of items
cost_of_rice = 52  # per kg
cost_of_wheat = 34  # per kg

# quantity of items
qty_of_rice = float(input('Enter qty of rice(loosely):'))
print('qty_of_rice', qty_of_rice, type(qty_of_rice))

qty_of_wheat = int(input('Enter qty of wheat needed:'))
print('qty_of_wheat', qty_of_wheat, type(qty_of_wheat))

# data type converters: int(), float(), str()

# Total Amount
total_amount = cost_of_rice * qty_of_rice + cost_of_wheat * qty_of_wheat
print('Total Amount :', total_amount)
