#!/usr/bin/python
"""
Purpose: Single Inheritance
MRO - method resolution order
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
            return "buddy !!! you need to maintain a minimum balance"
        else:
            Account.withdraw(self, amount)


mb = MinBalanceAccount()

print(dir(mb))

print('mb.balance      ', mb.balance)
print('mb.deposit(10)  ', mb.deposit(10))
print('mb.balance      ', mb.balance)
print('mb.withdraw(100)', mb.withdraw(100))

print('=================================')

# Main
# student
will_smith = MinBalanceAccount()
print("Initial balance of will_smith {}".format(will_smith.balance))
will_smith.deposit(2000)
print("balance of will_smith {}".format(will_smith.balance))
will_smith.withdraw(500)
print("balance of will_smith {}".format(will_smith.balance))
will_smith.withdraw(600)
print("balance of will_smith {}".format(will_smith.balance))

# working
federer = Account()
print("Initial balance of federer {}".format(federer.balance))
federer.deposit(2000)
print("balance of federer {}".format(federer.balance))
federer.withdraw(500)
print("balance of federer {}".format(federer.balance))
federer.withdraw(600)
print("balance of federer {}".format(federer.balance))
