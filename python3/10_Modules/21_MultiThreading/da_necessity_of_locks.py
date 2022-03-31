import threading
deposit = 100


def add_profit():
    """ Function to add profit to the deposit"""
    global deposit
    for i in range(100000):
        deposit = deposit + 10


def pay_bill():
    """ Function to deduct money from the deposit"""
    global deposit
    for i in range(100000):
        deposit = deposit - 10


# Creating threads
thread1 = threading.Thread(target=add_profit, args=())
thread2 = threading.Thread(target=pay_bill, args=())

# Starting the threads
thread1.start()
thread2.start()

# Waiting for both the threads to finish executing
thread1.join()
thread2.join()

# Displaying the final value of the deposit
print(deposit)
