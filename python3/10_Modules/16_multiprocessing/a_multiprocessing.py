import os
from multiprocessing import Process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print("{0:2} doubled to {1:2} by process id: {2:6}".format(number, result, proc))


if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for number in numbers:
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    # Joining processes, to tell python to wait for the proces to terminate
    for proc in procs:
        proc.join()
