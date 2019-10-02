#!python -u
"""
Purpose:Electricity Board Current Bill Slab rates
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
         60 + 40 + 50 + 100 + 157
                    
"""
__author__ = 'Python Tutor'

units_consumed = float(input('Enter the units consumed:'))

print(f'You consumed {units_consumed} units electricity')

if units_consumed > 250:
    amount = (60 * 1.25) + (40 * 2.0) + (50 * 4.0) + (100 * 7.0) + ((units_consumed - 250) * 10)
elif 150 < units_consumed <= 250:
    amount = (60 * 1.25) + (40 * 2.0) + (50 * 4.0) + ((units_consumed - 150) * 7.0)
elif 100 < units_consumed <= 150:
    amount = (60 * 1.25) + (40 * 2.0) + ((units_consumed - 100) * 4.0)
elif 60 < units_consumed <= 100:
    amount = (60 * 1.25) + ((units_consumed - 60) * 2.0)
else:  # < 60
    amount = (units_consumed * 1.25)

print(f'amount:{amount}')
