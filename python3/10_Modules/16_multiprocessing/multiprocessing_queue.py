#!/usr/bin/python3
"""
Purpose: Multiprocessing using Queues

Queue objects are a FIFO data structure that are
thread and process safe which make them perfect
for passing data between different processes
    without potentially corrupting data.
"""
from multiprocessing import Process, Queue
import random


def rand_num(queue):
    num = random.random()
    queue.put(num)


if __name__ == "__main__":
    queue = Queue()

    processes = [Process(target=rand_num, args=(queue,)) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for p in processes]

    print(results)
