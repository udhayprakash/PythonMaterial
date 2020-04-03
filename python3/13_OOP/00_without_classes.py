#!/usr/bin/python
"""
Purpose: without OOPS, solving a problem
"""
balance = 0


def deposit(amount):
    global balance
    balance += amount
    return balance


def withdraw(amount):
    global balance
    balance -= amount
    return balance


if __name__ == '__main__':
    # Akhila
    print(f"Akhila - initial balance {balance}")
    deposit(1000)
    print(f"Akhila - After salary    {balance}")
    withdraw(300)
    print(f"Akhila - After withdrawl {balance}")

    # Neha
    print(f"\nNeha   - initial balance {balance}")
