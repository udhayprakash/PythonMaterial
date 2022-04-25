import random
import threading
import time


class ThreadWithResult(threading.Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None
    ):
        def function():
            self.result = target(*args, **kwargs)

        super().__init__(group=group, target=function, name=name, daemon=daemon)


def function_to_thread(n):
    count = 0
    while count < 3:
        print(f"still running thread {n}")
        count += 1
        time.sleep(3)
    result = random.random()
    print(f"Return value of thread {n} should be: {result}")
    return result


def main():
    thread1 = ThreadWithResult(target=function_to_thread, args=(1,))
    thread2 = ThreadWithResult(target=function_to_thread, args=(2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(thread1.result)
    print(thread2.result)


main()
