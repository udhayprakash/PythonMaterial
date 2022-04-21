#!/usr/bin/python3
import time


def retry_on_failure(max_attempts=5):
    attempt = 0
    times = (1, 1, 2, 3, 5, 8)

    def inner(func):
        def wrapper(*args, **kwargs):
            nonlocal attempt
            while attempt < max_attempts:
                try:
                    result = func(*args, **kwargs)
                except Exception as ex:
                    print(ex)
                    print(f"\tWaiting for {times[attempt]} seconds ...")
                    time.sleep(times[attempt])
                    attempt += 1
                else:
                    return result

        return wrapper

    return inner


@retry_on_failure(5)
def myfunc():
    print("\nmyfunc - start")
    1 / 0


myfunc()
