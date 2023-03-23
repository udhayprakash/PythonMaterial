#!/usr/bin/python


# This multithreading program creates five threads
# and each thread prints "Hello World" with a two-second interval


import threading
import time


def hello_world(num):
    """User defined thread function"""
    time.sleep(num)
    print("Hello World", num)


threads = []  # Threads list needed when we use a bulk of threads
print("Program started.  This program will print Hello World five times...")
for i in range(5, 0, -1):
    mythread = threading.Thread(target=hello_world, args=(i,))
    threads.append(mythread)
    # time.sleep(2)
    mythread.start()

for thread in threads:  # iterates over the threads
    thread.join()  # waits until the thread has finished work

print("Done! Program ended")
