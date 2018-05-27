#!python -u
"""
Purpose:Electricity Board Current Bill Slab rates 
"""
__author__ = 'Python Tutor'

name = str(raw_input ("Please enter your name: "))
number = int(raw_input ("Please enter service number?: "))
units = int(raw_input ("How many units consumed?: "))

if units < 50:
    amt = 3*units
elif units > 50 and units < 100:
    amt = ((5 * (units - 50)) + 150)
elif units > 100 and units < 150:
    amt = ((7 * (units - 100)) + 400)
elif units > 150:
    amt = ((10 * (units - 150)) + 750)
else :
    amt = 'undefined'
    
print(("Total taxable amount Rs: %d/-")%(amt))    
print("Service tax is 14.5%")
print(("Customer %s with service number %d has to pay Rs. %d /-")%(name, number, (amt+amt*14.5/100.00)))
