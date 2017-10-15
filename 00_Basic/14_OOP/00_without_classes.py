#!/usr/bin/python

balance=0

def deposit(amount):
  global balance
  balance = balance + amount
  return balance
  
def withdraw(amount):
  global balance
  balance = balance - amount
  return balance
  
# Main

# kumar
print "my initial balance {}".format(balance)
deposit(1000)
print "my balance after dads deposit {}".format(balance)
withdraw(300)
print "my balance after movie is {}".format(balance)

# yash
print "my initial balance {}".format(balance)
	