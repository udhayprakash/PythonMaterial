#!/usr/bin/python

def new():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] = account['balance'] + amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] = account['balance'] - amount
    return account['balance']


# kumar
kumar = new()
print "The basic amount for kumar {}".format(kumar['balance'])
deposit(kumar, 1000)
print "The  amount for kumar {} after deposit".format(kumar['balance'])
withdraw(kumar, 300)

# yash
yash = new()
print "The basic amount for yash {}".format(yash['balance'])
deposit(yash, 2000)
print "The  amount for yash {} after deposit".format(yash['balance'])
withdraw(yash, 300)

print "The  amount for kumar {} after withdraw".format(kumar['balance'])
print "The  amount for yash {} after withdraw".format(yash['balance'])
