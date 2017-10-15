#!/usr/bin/python
"""
Purpose: Single Inheritance
"""


class Account:
    """
    parent class
    """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance


class MinBalanceAccount(Account):
    """
    child class
    """

    def __init__(self):
        Account.__init__(self)

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print "buddy !!! you need to maintain a minimum balance"
        else:
            Account.withdraw(self, amount)


# Main
# student
shiva = MinBalanceAccount()
print "Initial balance of shiva {}".format(shiva.balance)
shiva.deposit(2000)
print "balance of shiva {}".format(shiva.balance)
shiva.withdraw(500)
print "balance of shiva {}".format(shiva.balance)
shiva.withdraw(600)
print "balance of shiva {}".format(shiva.balance)

# working
kanth = Account()
print "Initial balance of kanth {}".format(kanth.balance)
kanth.deposit(2000)
print "balance of kanth {}".format(kanth.balance)
kanth.withdraw(500)
print "balance of kanth {}".format(kanth.balance)
kanth.withdraw(600)
print "balance of kanth {}".format(kanth.balance)

# https://www.edx.org/
