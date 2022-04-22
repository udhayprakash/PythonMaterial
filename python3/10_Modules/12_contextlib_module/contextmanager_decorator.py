from contextlib import contextmanager
from time import sleep, time


@contextmanager
def timed(label):
    start = time()  # Setup - __enter__
    print(f"{label}: Start at {start}")
    try:
        yield  # yield to body of `with` statement
    finally:  # Teardown - __exit__
        end = time()
        print(f"{label}: End at {end} ({end - start} elapsed)")


with timed("Counter"):
    sleep(3)

# Counter: Start at 1599153092.4826472
# Counter: End at 1599153095.4854734 (3.00282621383667 elapsed)
