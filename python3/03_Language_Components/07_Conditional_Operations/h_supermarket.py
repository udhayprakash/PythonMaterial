#!/usr/bin/python
"""
Purpose: print different amount based on various customer types
"""
__name__ = 'Author'

apple = 10
mango = 5
sugar = 25
oil = 20
# discount 30% on fruit and 10% on oil

name = input("Please enter your name: ")
customer = str(input("what type of customer(regular or lucky or nocredit): "))  #
a_qty = int(input("how many apple(s): "))
m_qty = int(input("how many mango(es): "))
s_qty = int(input("how many kg(s) sugar: "))
o_qty = int(input("how many liter(s) oil: "))

if customer == 'regular':
    amt = (((a_qty * apple + m_qty * mango) * .70) + s_qty * sugar + ((o_qty * oil) * .90))
    print(f"Hi {name}, the total amt you have to pay is ${amt}")
elif customer == 'lucky':
    amt = ((a_qty * apple + m_qty * mango + s_qty * sugar + o_qty * oil) * .80)
    print(f"Hi {name},  the total amt you have to pay is ${amt}")
elif customer == 'nocredit':
    amt = (a_qty * apple + m_qty * mango + s_qty * sugar + o_qty * oil)
    print(f"Hi {name}, the total amt you have to pay is ${amt}")
else:
    print("please enter correct type of customer")
