# !usr/bin/env python
# calculator program

# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice


def menu():
    # print what options you have

    print("==" * 15)
    print("Welcome to calculator.py")
    print("your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")
    return eval(input("Choose your option: "))


# this adds two numbers given
def add(a, b):
    print(a, "+", b, "=", a + b)


# this subtracts two numbers given
def sub(a, b):
    print(b, "-", a, "=", b - a)


# this multiplies two numbers given
def mul(a, b):
    print(a, "*", b, "=", a * b)


# this divides two numbers given
def div(a, b):
    print(a, "/", b, "=", a / b)


# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(eval(input("Add this: ")), eval(input("to this: ")))
    elif choice == 2:
        sub(eval(input("Subtract this: ")), eval(input("from this: ")))
    elif choice == 3:
        mul(eval(input("Multiply this: ")), eval(input("by this: ")))
    elif choice == 4:
        div(eval(input("Divide this: ")), eval(input("by this: ")))
    elif choice == 5:
        loop = 0

print("Thankyou for using calculator.py!")

# NOW THE PROGRAM REALLY FINISHES
