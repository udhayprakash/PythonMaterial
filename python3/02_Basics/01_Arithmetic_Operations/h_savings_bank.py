#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""
balance = 0
print("Initial Balance       :", balance)

# Initial account opening deposit of 1500
balance += 1500  # balance = balance + 1500
print("After initial Deposit :", balance)

# salary credited of 3300
balance += 3300
print("After Salary credited :", balance)

# Online Purchase of 33.33
balance -= 33.33
print("After Online purchase :", balance)

# House Rent of 1500 paid
balance -= 1500
print("After House Rent paid :", balance)

print("Final Balance         :", balance)
