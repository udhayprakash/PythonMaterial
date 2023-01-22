#!/usr/bin/python
"""
Purpose: without OOPS, solving a problem

    Problem - To create a saving bank with facilitates transactions

        customer 1
                                                Balance
            Account creation                        0
            Transaction 1 - deposit  1000        1000
            Transaction 2 - withdraw  200         800

        Customer 2
                                                Balance
            Account creation                        0
            Transaction 1 - deposit  3500        3500
            Transaction 2 - withdraw  550        2950

"""


def new():
    return {"balance": 0}


def deposit(account, amount):
    print(f"\tDeposited {amount}")
    account["balance"] += amount
    return account["balance"]


def withdraw(account, amount):
    print(f"\tWithdrawn {amount}")
    account["balance"] -= amount
    return account["balance"]


if __name__ == "__main__":
    # Priyanka
    Priyanka = new()  # {'balance': 0}
    print(f'Priyanka initial balance :{Priyanka["balance"]}')  # 0
    deposit(Priyanka, 1000)
    print(f'Priyanka current balance :{Priyanka["balance"]}')  # 1000

    deposit(Priyanka, 2500)
    print(f'Priyanka current balance :{Priyanka["balance"]}')

    withdraw(Priyanka, 750)
    print(f'Priyanka current balance :{Priyanka["balance"]}')

    print()
    # Varun
    Varun = new()
    print(f'Varun    initial balance :{Varun["balance"]}')

    deposit(Varun, 99)
    print(f'Varun    current balance :{Varun["balance"]}')
