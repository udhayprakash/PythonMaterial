# Using try/finally
import time

start = time.perf_counter()  # Setup
try:  # Actual body
    time.sleep(3)
finally:  # Teardown
    end = time.perf_counter()
    elapsed = end - start

print(elapsed)


# Using Context Manager
class Timer:
    def __init__(self):
        self._start = None
        self.elapsed = 0.0

    def start(self):
        if self._start is not None:
            raise RuntimeError("Timer already started...")
        self._start = time.perf_counter()

    def stop(self):
        if self._start is None:
            raise RuntimeError("Timer not yet started...")
        end = time.perf_counter()
        self.elapsed += end - self._start
        self._start = None

    def __enter__(self):  # Setup
        self.start()
        return self

    def __exit__(self, *args):  # Teardown
        self.stop()


with Timer() as t:
    time.sleep(3)

print(t.elapsed)


manager = Timer()
manager.__enter__()  # Setup
time.sleep(3)  # Body
manager.__exit__(None, None, None)  # Teardown
print(manager.elapsed)
