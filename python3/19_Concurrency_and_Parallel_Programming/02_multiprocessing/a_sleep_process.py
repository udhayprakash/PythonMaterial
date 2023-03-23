import multiprocessing
import os
import threading
import time


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(
        f"Task {task_number} done (slept for {sleep_duration}s)! "
        f"Process ID: {os.getpid()}"
    )


if __name__ == "__main__":
    # Sequential
    time_start = time.time()

    task_sleep(2, 1)
    task_sleep(2, 2)

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")
    print()

    time_start = time.time()

    # Create thread
    p1 = threading.Thread(target=task_sleep, args=(2, 1))
    p2 = threading.Thread(target=task_sleep, args=(2, 2))

    # Start task execution
    p1.start()
    p2.start()

    # Wait for thread to complete execution
    p1.join()
    p2.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")
    print()

    print()

    time_start = time.time()

    # Create process
    p1 = multiprocessing.Process(target=task_sleep, args=(2, 1))
    p2 = multiprocessing.Process(target=task_sleep, args=(2, 2))

    # Start task execution
    p1.start()
    p2.start()

    # Wait for process to complete execution
    p1.join()
    p2.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")
    print()


# Task 1 done (slept for 2s)! Process ID: 26944
# Task 2 done (slept for 2s)! Process ID: 26944
# Time elapsed: 4.0s

# Task 1 done (slept for 2s)! Process ID: 26944
# Task 2 done (slept for 2s)! Process ID: 26944
# Time elapsed: 2.0s


# Task 2 done (slept for 2s)! Process ID: 2888
# Task 1 done (slept for 2s)! Process ID: 12080
# Time elapsed: 2.15s
