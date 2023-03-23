"""
Purpose: Joining the threads to wait till all are completed
"""
import os
import threading


def task1():
    print(f"\nTask 1 assigned to thread   : {threading.current_thread().name}")
    print(f"ID of process running task 1: {os.getpid()}")


def task2():
    print(f"\nTask 2 assigned to thread   : {threading.current_thread().name}")
    print(f"ID of process running task 2: {os.getpid()}")


# print ID of current process
print(f"ID of process running main program: {os.getpid()}")

# print name of main thread
print(f"Main thread name: {threading.main_thread().name}")

# creating threads
t1 = threading.Thread(target=task1, name="t1")
t2 = threading.Thread(target=task2, name="t2")


# starting threads
t1.start()
t2.start()

# wait until all threads finish
t1.join()  # waits until t1 thread is completed
t2.join()  # waits until t2 thread is completed

print("END ==========")
