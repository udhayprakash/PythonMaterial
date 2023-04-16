#!/usr/bin/python3
"""
Purpose: Fruit Store

    Items   price       qty                         amount
    -----------------------------------------------------------
    Apples   12/piece   5 dozens = 5 * 12 = 60      12 * 60
    Mangos   34/piece   3 dozens = 3 * 12 = 36      34 * 36
                                                ---------------
                                                      1944   /-
                                discount     -2 %     - 38.88/-
                                                ---------------
                                                      1905.12/-
                                GST         +12.5 %   +238.14/-
                                                ---------------
                                                      2143.26/-
                                                ---------------


Algorithm
---------
Step 1:  Get the cost of fruits into variables
Step 2:  Get the quantity of fruits into variables.
         Compute the end quantity, by substituting dozen value.
Step 3:  Compute the selling price to each item,
         and add them
Step 4:  Compute the discount amount and subtract
         from the selling price, to create payable amount
Step 5:  Calculate GST amount and Add to payable amount,
         to create billable amount
"""
# Constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5

# cost of fruits
cost_of_apple = 12  # per piece
cost_of_mango = 34  # per piece


# Quantities of fruits
qty_of_apples = 5 * DOZEN  # pieces
qty_of_mangos = 3 * DOZEN  # pieces

# Selling Price Computation
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos  # PEDMAS
print("Total Selling Price :", total_sp)


# Discount Calculation
discount_amount = (total_sp * DISCOUNT) / 100
print("Discount Amount     :", discount_amount)

# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount      :", payable_amount)

# GST Calculation
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits       :", gst_on_fruits)

# Billable Amount Calculation
billable_amount = payable_amount + gst_on_fruits
print("Billable Amount     :", billable_amount)

# round(num, no_of_digits) - function
print("Billable Amount(r)  :", round(billable_amount, 2))
