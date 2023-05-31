"""
Purpose: Single Inheritance

    Parent - child classes relation
    Super - sub classes relation

NOTE: All child classes should make calls to the parent class
constructors
    MRO - method resolution order

"""


class Account:
    """
    Parent or super class
    """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


# a1 = Account()
# print(vars(a1))
# print(dir(a1))


class MinimumBalanceAccount(Account):
    """
    Child or sub class
    """

    def __init__(self):
        # calling the constructor of the parent class
        Account.__init__(self)

    def withdraw(self, amount):
        if self.balance - amount < 100:
            print("Please maintain minimum balance. transaction failed!!!")
        else:
            Account.withdraw(self, amount)


a2 = MinimumBalanceAccount()
print(vars(a2))  # {'balance': 0}
print(dir(a2))  # 'balance', 'deposit', 'withdraw'


# MRO - Method Resolution Order
print(Account.__mro__)
# (<class '__main__.Account'>, <class 'object'>)


print(MinimumBalanceAccount.__mro__)
# (<class '__main__.MinimumBalanceAccount'>, <class '__main__.Account'>, <class 'object'>)


print(f"Initial balance     :{a2.balance}")
print(dir(a2))
print()

a2.deposit(1300)
print(f"After deposit(1300) :{a2.balance}")

a2.withdraw(900)
print(f"After withdraw(900) :{a2.balance}")

a2.withdraw(400)
