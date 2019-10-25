#!/usr/bin/python
"""
Purpose: fruit store

    Items   price       qty                         amount
    ------------------------------------------------------
    Apples   12/piece   5 dozens = 5 * 12 = 60      12 * 60 
    Mangos   34/piece   3 dozens = 3 * 12 = 36      34 * 36
                                                -----------
                                        discount     2 %
                                        GST         12.5 %

"""
# constants
DOZEN = 12
GST = 12.5
DISCOUNT = 2

# Cost of fruits
cost_of_apple = 12 # per piece 
cost_of_mango = 34 # per piece

# Quantity of fruits
qty_of_apples = 5 * DOZEN
qty_of_mangos = 3 * DOZEN 

# # Selling Prices 
# sp_of_apples = cost_of_apple * qty_of_apples
# sp_of_mangos = cost_of_mango * qty_of_mangos

# # Total amount
# total_amount = sp_of_apples + sp_of_mangos

total_amount = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos
print('Total Amount     :', total_amount)

# Discount 
# discount = (total_amount * DISCOUNT)/ 100
discount = total_amount * DISCOUNT/ 100
print('Discount Amount  :', discount)

# payable amount 
payable_amount = total_amount - discount
print('payable_amount   :', payable_amount)

# GST calculation
gst_on_fruits = (payable_amount * GST)/ 100
print('GST Amount       :', gst_on_fruits)

# Billable Amount
billable_amount = payable_amount - gst_on_fruits
print('Billable Amount  :', billable_amount)