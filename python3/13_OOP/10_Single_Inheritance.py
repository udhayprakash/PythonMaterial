#!/usr/bin/python
"""
Purpose: Single Inheritance
    MRO - method resolution order

Parent - Child classes relation
Super - Sub classes relation

All child classes should make calls to the parent class
constructors
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


# a1 = Account()
# # print(vars(a1))
# print(dir(a1))


class MinimumBalanceAccount(Account):
    """
        child or sub class
    """

    def __init__(self):
        # calling the constructor of the parent class
        Account.__init__(self)

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            print("PLease maintain minimum balance. transaction failed!!!")
        else:
            Account.withdraw(amount)


a2 = MinimumBalanceAccount()
print(dir(a2))

print(f'Initial balance     :{a2.balance}')
a2.deposit(1300)
print(f'After deposit(1300) :{a2.balance}')

a2.withdraw(900)
print(f'After withdraw(900) :{a2.balance}')
