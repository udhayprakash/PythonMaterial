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


def creat_account():
    return {"balance": 0}


def deposit(account, amount):
    print(f"\tDeposited {amount}")
    # balance += amount
    account["balance"] += amount


def withdraw(account, amount):
    print(f"\tWithdrawn {amount}")
    # balance -= amount
    account["balance"] -= amount


if __name__ == "__main__":
    # Priyanka
    Priyanka = creat_account()  # {'balance': 0}
    print(f'Priyanka initial balance :{Priyanka["balance"]}')  # 0
    deposit(Priyanka, 1000)
    print(f'Priyanka current balance :{Priyanka["balance"]}')  # 1000

    deposit(Priyanka, 2500)
    print(f'Priyanka current balance :{Priyanka["balance"]}')

    withdraw(Priyanka, 750)
    print(f'Priyanka current balance :{Priyanka["balance"]}')

    print("----------------------------------------")
    # UDahy
    udhay = creat_account()
    print(f'udhay initial balance :{udhay["balance"]}')  # 0
    deposit(udhay, 1000)
    print(f'udhay current balance :{udhay["balance"]}')  # 1000
