#!/usr/bin/python
"""
Purpose: Single Inheritance
"""


class Account:
    """
    parent or super class
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
    child or sub class
    """

    def __init__(self):
        Account.__init__(self)  # calling the constructor of the parent class

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print "buddy !!! you need to maintain a minimum balance"
        else:
            Account.withdraw(self, amount)



mb = MinBalanceAccount()

print dir(mb)

print 'mb.balance', mb.balance
print 'mb.deposit(10)', mb.deposit(10)
print 'mb.balance', mb.balance
print 'mb.withdraw(100)', mb.withdraw(100)

print '================================='

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

# # https://www.edx.org/
