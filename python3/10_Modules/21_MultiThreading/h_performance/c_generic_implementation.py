#!/usr/bin/python3
import argparse
import sys
import threading
import time


def main():
    # Parser arguments
    parser = argparse.ArgumentParser(description="Multi-threading counter. By IceM4nn")
    parser.add_argument(
        "thread", help="State the number of concurrent thread.", type=int
    )
    parser.add_argument(
        "count",
        help="State the number count value for the thread. The number in count will decrement until it reaches 0.",
        type=int,
    )
    parser.add_argument(
        "-s",
        "--synchronize",
        help="Run the thread with synchronize. Default is false",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--delay",
        help="Give a delay to threads in seconds. Default is 2",
        default=2,
        type=int,
    )
    args = parser.parse_args()

    # Initialize the arguments
    threadNumber = args.thread
    count = args.count
    synchronize = args.synchronize
    delay = args.delay

    # Test the arguments, to avoid problems
    if threadNumber <= 0 or count <= 0 or delay <= 0:
        print("[!] Argument cannot be zero or less than zero. Exiting")
        sys.exit(2)

    # Print out current settings
    print("[i] You have specify", threadNumber, "number of thread(s).")
    print("[i] Every thread will count", count, "concurrently until it reaches 0.")
    print("[i] Synchronize is set to", synchronize)
    print("[i] Delay value is", delay, "seconds\n")

    # Initialize threadNumber in a list
    threadCount = []
    while threadNumber > 0:
        threadCount.append(threadNumber)
        threadNumber -= 1
    threadCount.reverse()

    # Initialize threads into a list threads
    threads = []
    # Create new threads
    for i in threadCount:
        i = MyThread(i, "Thread-" + str(i), count, synchronize, delay)
        threads.append(i)

    # Start new Threads
    for i in threads:
        i.start()

    # Wait for all threads to complete
    for i in threads:
        i.join()

    print("Done. Exiting Main Thread")


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter, synchronize, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.synchronize = synchronize
        self.delay = delay

    def run(self):
        print("[+] Starting " + self.name)
        threadLock = threading.Lock()

        # Get lock to synchronize threads
        if self.synchronize:
            threadLock.acquire()

        print_time(self.name, self.delay, self.counter)

        # Free lock to release next thread
        if self.synchronize:
            threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == "__main__":
    main()
