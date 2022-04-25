#!/usr/bin/python
"""
Purpose: To display thread names

    In CPython, due to the Global Interpreter Lock, only one thread
    can execute Python code at once.
    To make better use of computational resources of multi-core machines,
    you are advised to use multiprocessing or
    concurrent.futures.ProcessPoolExecutor.

    However, threading is still an appropriate model if you want to run
    multiple I/O-bound tasks simultaneously.
"""
import threading


def hello_world():
    print(threading.current_thread().name, "Starting")
    print("\tHello World")
    print(threading.current_thread().name, "Exiting")


def greetings():
    print(threading.current_thread().name, "Starting")
    print("\tGood Morning")
    print(threading.current_thread().name, "Exiting")


# Creating threads
hw_thread = threading.Thread(target=hello_world)  # , name='HelloWorld')
greet_thread = threading.Thread(target=greetings)  # , name='Greetings')


print(f"Before Starting:{threading.active_count() =}")  # main thread

# starting threads
hw_thread.start()
greet_thread.start()

print(f"After Starting:{threading.active_count() =}")  # 1(main) + 2 = 3

print("END===")
