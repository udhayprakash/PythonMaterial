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
balance = 0


def deposit(amount):
    global balance
    print(f"\tDeposited {amount}")
    balance = balance + amount
    return balance


def withdrawl(amount):
    global balance
    print(f"\tWithdrawn {amount}")
    balance = balance - amount
    return balance


if __name__ == "__main__":
    # Sudha
    print(f"\nSudha initial balance   :{balance}")

    deposit(1000)
    print(f"nSudha's current balance :{balance}")

    withdrawl(200)
    print(f"nSudha's current balance :{balance}")
    print("----------------------------------------")

    # Sai
    print(f"\nSai initial balance   :{balance}")
