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

The pool is responsible for a fixed number of threads.

    - It controls when the threads are created, such as just-in-time when they are needed.
    - It also controls what threads should do when they are not being used, such as making them wait without consuming computational resources.

"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor


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
    # To limit to max 3 workers, at a time
    # REUSAGES those threads, instead of creating new threads
    # task1 = executor.submit(task)

    for _ in range(10):
        time.sleep(1)
        executor.submit(task)


if __name__ == "__main__":
    main()
