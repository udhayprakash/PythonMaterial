#!/usr/bin/python
"""
Purpose: Electricity Board Current Bill Slab rates
    
    electricity bill slabs
    -----------------------
	0 till 60   ===> 1.25
	60 till 100  ===> 2.00
	100 till 150 ===> 4.00
	150 till 250 ===> 7.00
	250 +        ===> 10

electricity cess : 2%
discount         : -1.11%

GST              : 7%

units consumed : 357
         60     +   40      + 50    + 100    + 157
         1.25/- + 2.00/-    + 4.00/-+ 7.00/- + 10/-

"""
# units_consumed = 357
units_consumed = float(input('Enter the no. of units consumed:'))
remaining_units = units_consumed


if remaining_units < 0:
    print('Invalid Input')
else:
    amount = 0
    if remaining_units > 250:
        slab_units = remaining_units - 250
        amount += slab_units * 10.0
        remaining_units = 250

    if 150 < remaining_units <= 250:
        slab_units = remaining_units - 100
        amount += slab_units * 7.0 
        remaining_units = 150

    if 100 < remaining_units <= 150:
        slab_units = remaining_units - 50
        amount += slab_units * 4.0
        remaining_units = 100

    if 60 < remaining_units <= 100:
        slab_units = remaining_units - 40
        amount += slab_units * 2.0 
        remaining_units = 60 

    if 0 < remaining_units <= 60:
        amount += remaining_units * 1.25

    print(f'''
        Units Consumed : {units_consumed}
        Amount Payable : Rs. {amount} /-
    ''')

# Assignment - SOlve the remaining problem 
