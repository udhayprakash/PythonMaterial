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

Algorithm
----------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items into variables
Step 3: Compute the selling price to each item, and add them
Step 4: Compute the subsidy amount and subtract from the selling price
Step 5: Display the billable amount
"""
# cost of Items
cost_of_wheat = 25  # per kg
cost_of_rice = 12  # per kg

# Quantities of Items
qty_of_wheat = 30  # kgs
qty_of_rice = 50  # kgs

# Selling Prices computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
print('total Selling Price:', total_sp)

# Calculating the subsidy of 20 %
subsidy_amount = (total_sp * 20) / 100
print('Subsidy Amount     :', subsidy_amount)

# Billable amount calculation
billable_amount = total_sp - subsidy_amount
print('Billable Amount    :', billable_amount)
