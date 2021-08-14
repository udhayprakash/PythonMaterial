#!/usr/bin/python3
"""
Purpose:
- ThreadPoolExecutors provide a simple abstraction 
around spinning up multiple threads and using 
these threads to perform tasks in a concurrent 
fashion. 
- Adding threading to your application can help to 
drastically improve the speed of your application 
when used in the right context.
- By using multiple threads we can speed up applications
which face an input/output based bottleneck, a good 
example of this would be a web crawler.
"""
from concurrent.futures import ThreadPoolExecutor
import threading


def task():
    print("Executing our Task")
    result = 0
    i = 0
    for i in range(10):
        result = result + i
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()
