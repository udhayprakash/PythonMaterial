#!python -u 
"""
Purpose:print different amount based on various customer types
"""

apple = 10
mango = 5
sugar = 25
oil = 20
#discount 30% on fruit and 10% on oil

name = raw_input("Please enter your name: ")
customer = str(raw_input("what type of customer: "))   #regular or lucky or nocredit
a_qty = int(raw_input("how many apple(s): "))
m_qty = int(raw_input("how many mango(es): "))
s_qty = int(raw_input("how many kg(s) sugar: "))
o_qty = int(raw_input("how many liter(s) oil: "))

if customer == 'regular':
    amt = (((a_qty*apple + m_qty*mango)*.70) + s_qty*sugar + ((o_qty*oil )*.90))
    print (("Hi %s, the total amt you have to pay is $%d")%(name, amt))
elif customer == 'lucky':
    amt = ((a_qty*apple + m_qty*mango + s_qty*sugar + o_qty*oil )*.80)
    print (("Hi %s,  the total amt you have to pay is$%d")%(name,amt))
elif customer == 'nocredit':
    amt = (a_qty*apple + m_qty*mango + s_qty*sugar + o_qty*oil)
    print (("Hi %s, the total amt you have to pay is$%d")% (name,amt))
else:
    print ("please enter type of customer")
