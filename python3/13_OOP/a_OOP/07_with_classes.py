#!/usr/bin/python
"""
Purpose: Solving Bank account management problem, using classes
"""


class Account:
    def __init__(self, name):
        self.balance = 0
        self.account_holder = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        return f"Account Balance for {self.account_holder} is {self.balance}"


if __name__ == "__main__":
    shurti = Account("shruti")
    print(vars(shurti))
    print("Initially", shurti.display_balance())
    shurti.deposit(1000)
    print("After Deposit", shurti.display_balance())
    shurti.withdraw(400)
    print("After withdrawl", shurti.display_balance())

    print("----------------------------")
    semona = Account("semona")
    print(vars(semona))
    print("Initially", semona.display_balance())
    semona.deposit(300)
    print("After Deposit", semona.display_balance())
    semona.withdraw(100)
    print("After withdrawl", semona.display_balance())
