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
GST              : 7%

discount         : -1.11%

units consumed : 357


	60 + 40 + 50 + 100 + 107
"""
__author__ = 'Python Tutor'

name = str(raw_input("Please enter your name: "))
number = int(raw_input("Please enter service number?: "))
units = int(raw_input("How many units consumed?: "))

if units < 60:
    amt = 3 * units
elif units > 60 and units < 100:
    amt = ((5 * (units - 50)) + 150)
elif units > 100 and units < 150:
    amt = ((7 * (units - 100)) + 400)
elif units > 150:
    amt = ((10 * (units - 150)) + 750)
else:
    amt = 'undefined'

print(("Total taxable amount Rs: %d/-") % (amt))
print("Service tax is 14.5%")
print(("Customer %s with service number %d has to pay Rs. %d /-") % (name, number, (amt + amt * 14.5 / 100.00)))
