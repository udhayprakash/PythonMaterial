#!/usr/bin/python
"""
Purpose:
"""
import concurrent.futures
import time


def slow_op(*args):
    print(f"arguments: {args}")
    time.sleep(5)
    print("slow operation complete")
    return 123


def do_something():
    with concurrent.futures.ProcessPoolExecutor() as pool:
        future = pool.submit(slow_op, "a", "b", "c")

        for fut in concurrent.futures.as_completed([future]):
            assert future.done() and not future.cancelled()
            print(f"got the result from slow_op: {fut.result()}")


if __name__ == "__main__":
    print("program started")
    do_something()
    print("program complete")
