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
    neha = Account("Neha")
    print(vars(neha))
    print("Initially", neha.display_balance())

    neha.deposit(1000)
    print("After Deposit", neha.display_balance())

    neha.withdraw(300)
    print("After withdraw", neha.display_balance())

    # ----------
    hiral = Account("Hiral")
    print("\n\n", vars(hiral))
    print("Initially", hiral.display_balance())

    hiral.deposit(2500)
    print("After Deposit", hiral.display_balance())

    hiral.withdraw(400)
    print("After withdraw", hiral.display_balance())
