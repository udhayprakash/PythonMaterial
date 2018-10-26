#!/usr/bin/python

def new():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] = account['balance'] + amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] = account['balance'] - amount
    return account['balance']


# Madhavi
Madhavi = new()
print "The basic amount for Madhavi {}".format(Madhavi['balance'])
deposit(Madhavi, 1000)
print "The  amount for Madhavi {} after deposit".format(Madhavi['balance'])
withdraw(Madhavi, 300)
print

# yash
yash = new()
print "The basic amount for yash {}".format(yash['balance'])
deposit(yash, 2000)
print "The  amount for yash {} after deposit".format(yash['balance'])
withdraw(yash, 300)

print "The  amount for Madhavi {} after withdraw".format(Madhavi['balance'])
print "The  amount for yash {} after withdraw".format(yash['balance'])
