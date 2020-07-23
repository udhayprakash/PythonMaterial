#!/usr/bin/python3
"""
Purpose: Grocery Store 

    Item       cost         
    ------------------------
    rice        10/kg       
    wheat       34/kg       

Algorithm
----------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input() 
        -> to get value in run-time
        -> will give any input as string only
"""
# cost of items
cost_of_rice = 10  # per kg
cost_of_wheat = 34  # per kg

# Quantities of Items
qty_of_rice = input('Enter Qty. of Rice  (in Kgs):')
qty_of_rice = int(qty_of_rice)
print('Qty of Rice  :', qty_of_rice, type(qty_of_rice))

# qty_of_wheat = input('Enter Qty. of Wheat(in Kgs):')
# qty_of_wheat = int(qty_of_wheat)

qty_of_wheat = int(input('Enter Qty. of Wheat(in Kgs):'))

print('Qty of Wheat :', qty_of_wheat, type(qty_of_wheat))

# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print('SP of Rice   :', sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print('SP of Wheat  :', sp_of_wheat)

total_sp = sp_of_rice + sp_of_wheat
print('Total SP     :', total_sp)