"""
Purpose: To list active threads
"""
import threading
import time


def my_function(seconds):
    print(f"my_function sleeps for {seconds} seconds")
    time.sleep(seconds)
    print("my_function finished")


def list_active_threads():
    print("Current Thread count: %i." % threading.active_count())
    print("Active Threads:")
    for thread in threading.enumerate():
        print("\tThread name is %s." % thread.name)


list_active_threads()

t1 = threading.Thread(target=my_function, args=(1,))
list_active_threads()

t1.start()
list_active_threads()

print("=================================")
for i in range(5):
    t2 = threading.Thread(target=my_function, args=(i,))
    t2.start()
    # t2.join()  # will make sequential run

list_active_threads()
