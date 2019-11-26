#!/usr/bin/python

# OOP 
# - code reusability 
# - modularity 

balance = 0


def deposit(amount):
    global balance
    balance = balance + amount
    return balance


def withdraw(amount):
    global balance
    balance = balance - amount
    return balance


if __name__ == '__main__':
    # Madhavi
    print("Madhavi -  initial balance {}".format(balance))
    deposit(1000)
    print("Madhavi -  balance after dads deposit {}".format(balance))
    withdraw(300)
    print("Madhavi -  balance after movie is {}".format(balance))

    # yash
    print("\nyash -  initial balance {}".format(balance))
