#!/usr/bin/python
"""
Purpose: without OOPS, solving a problem
"""


def new():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']


if __name__ == '__main__':
    Akhila = new()
    print(f"Akhila - initial balance {Akhila['balance']}")
    deposit(Akhila, 1000)
    print(f"Akhila - After salary    {Akhila['balance']}")
    withdraw(Akhila, 300)
    print(f"Akhila - After withdrawl {Akhila['balance']}")

    Neha = new()
    print(f"\nNeha   - initial balance {Neha['balance']}")
    deposit(Neha, 2300)
    print(f"Neha - After scolarship  {Neha['balance']}")
