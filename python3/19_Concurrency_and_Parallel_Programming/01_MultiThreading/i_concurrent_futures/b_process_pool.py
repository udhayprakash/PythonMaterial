import os
import time
from concurrent.futures import ProcessPoolExecutor


def task():
    print("Executing our Task on Process {}".format(os.getpid()))


def main():
    executor = ProcessPoolExecutor(max_workers=3)
    # pool some processes, and reuse them, instead of using new process

    # task1 = executor.submit(task)

    for _ in range(10):
        time.sleep(1)
        executor.submit(task)


if __name__ == "__main__":
    main()
