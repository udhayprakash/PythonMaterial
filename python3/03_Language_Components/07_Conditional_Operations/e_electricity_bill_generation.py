#!/usr/bin/python
"""
Purpose: Electricity Board Current Bill Slab rates
electricity bill

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


# units_consumed = 60
units_consumed = float(input('Enter the no. of units consumed:'))

amount = 0
if 0 <= units_consumed < 60:
    amount = units_consumed * 1.25
elif 60 <= units_consumed < 100:
    amount = 60 * 1.25 + (units_consumed - 60) * 2.0
elif 100 <= units_consumed < 150:
    amount = 60 * 1.25 + 40 * 2.0 + (units_consumed - 100) * 4.0
elif 150 <= units_consumed < 250:
    amount = 60 * 1.25 + 40 * 2.0 + 50 * 4.0 + (units_consumed - 150) * 7.0
elif units_consumed >= 250:
    amount = 60 * 1.25 + 40 * 2.0 + 50 * 4.0 + 100 * 7.0 + (units_consumed - 250) * 10.0
else:
    print('Invalid Entry')

print(f'''
    Units Consumed : {units_consumed}
    Amount Payable : Rs. {amount} /-
''')

# Assignment
# Complete the remaining part
