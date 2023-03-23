import time
from multiprocessing import Lock, Process, RawValue


class Counter(object):
    def __init__(self, value=0):
        # RawValue because we don't need it to create a Lock:
        self.val = RawValue("i", value)
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.val.value += 1

    def value(self):
        with self.lock:
            return self.val.value


def inc(counter):
    for i in range(1000):
        counter.increment()


if __name__ == "__main__":
    thread_safe_counter = Counter(0)
    procs = [Process(target=inc, args=(thread_safe_counter,)) for i in range(100)]

    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(thread_safe_counter.value())
