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
# balance = 0


def create_account():
    return {"balance": 0}


def deposit(account, amount):
    print(f"\tDeposited {amount}")
    # balance = balance + amount
    account["balance"] = account["balance"] + amount


def withdrawl(account, amount):
    print(f"\tWithdrawn {amount}")
    # balance = balance - amount
    account["balance"] = account["balance"] - amount


if __name__ == "__main__":
    # Sudha
    sudha = create_account()  # {'balance': 0}
    print(f"\nSudha initial balance   :{sudha['balance']}")

    deposit(sudha, 1000)  # {'balance': 1000}
    print(f"nSudha's current balance :{sudha['balance']}")

    withdrawl(sudha, 200)  # {'balance': 800}
    print(f"nSudha's current balance :{sudha['balance']}")
    print("----------------------------------------")

    # Sai
    sai = create_account()  # {'balance': 0}
    print(f"\nSai initial balance   :{sai['balance']}")

    deposit(sai, 3500)  # {'balance': 3500}
    print(f"sai's current balance :{sai['balance']}")

    withdrawl(sai, 550)  # {'balance': :2950}
    print(f"sai's current balance :{sai['balance']}")
