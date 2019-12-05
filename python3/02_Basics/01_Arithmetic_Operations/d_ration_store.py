#!/usr/bin/python
"""
Purpose: Ration store

    -----------------------------------------------
    item    cost        quantity        Amount
    -----------------------------------------------
    wheat   25/kg       30 kgs      25 * 30 = 750/- 
    Rice    12/kg       50 kgs      12 * 50 = 600/-
                                -------------------
                                              1350/-
                                subsidy 20%   -270/-
                                --------------------
                                BillableAmount:1080/-
"""
# cost of items
cost_of_wheat_in_kgs = 25
cost_of_rice_in_kgs = 12

# quantities of items
qty_of_wheat_in_kgs = 30
qty_of_rice_in_kgs = 50

# Selling price
sp_of_wheat = cost_of_wheat_in_kgs * qty_of_wheat_in_kgs  # 25 * 30 =750
sp_of_rice = cost_of_rice_in_kgs * qty_of_rice_in_kgs

# Total amount calculation
total_amount = sp_of_wheat + sp_of_rice
print('Total amount to pay  :', total_amount)

# subsidy of 20 %
subsidy_amount = (total_amount * 20)/ 100
print('subsidy_amount       :', subsidy_amount)

# Billable Amount
billable_amount = total_amount - subsidy_amount
print('billable_amount      :', billable_amount)