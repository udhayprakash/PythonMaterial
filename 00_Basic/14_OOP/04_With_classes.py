#!/usr/bin/python

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance


# Zero balance account
# main

sam = Account()
krish = Account()

print 'dir(sam)', dir(sam)

print 'sam.balance', sam.balance
print 'krish.balance', krish.balance

# Deposit
sam.deposit(1000)   # deposit(sam, 1000)  -- deposit(self, amount)
krish.deposit(10000)

print "after deposit"
print 'sam.balance', sam.balance
print 'krish.balance', krish.balance

# Withdraw
sam.withdraw(300)
krish.withdraw(3000)

print "after withdraw"
print 'sam.balance', sam.balance
print 'krish.balance', krish.balance