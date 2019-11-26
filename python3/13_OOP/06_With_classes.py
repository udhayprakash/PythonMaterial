#!/usr/bin/python
"""
Purpose:
"""


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


if __name__ == '__main__':
    teju = Account()
    rehman = Account()

    print(f'teju.balance    :{teju.balance}')
    print(f'rehman.balance  :{rehman.balance}')

    teju.deposit(1200)
    rehman.deposit(25)

    print()
    print(f'teju.balance    :{teju.balance}')
    print(f'rehman.balance  :{rehman.balance}')

    teju.withdraw(500)
    rehman.withdraw(12)

    print()
    print(f'teju.balance    :{teju.balance}')
    print(f'rehman.balance  :{rehman.balance}')
