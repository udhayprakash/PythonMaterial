#!usr/bin/env python

#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

# loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while True: #loop == 1:
    #print what options you have
    print "================================"*2
    print "Welcome to calculator.py"

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit calculator.py"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        add1 = input("Add this: ")
        add2 = input("to this: ")
        print add1, "+", add2, "=", add1 + add2
    elif choice == 2:
        sub2 = input("Subtract this: ")
        sub1 = input("from this: ")
        print sub1, "-", sub2, "=", sub1 - sub2
    elif choice == 3:
        mul1 = input("Multiply this: ")
        mul2 = input("with this: ")
        print mul1, "*", mul2, "=", mul1 * mul2
    elif choice == 4:
        div1 = input("Divide this: ")
        div2 = input("by this: ")
        print div1, "/", div2, "=", div1 / div2
    elif choice == 5:
        break #loop = 0
	
print "Thankyou for using calculator.py!"
