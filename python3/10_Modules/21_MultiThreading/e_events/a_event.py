"""
Purpose: Synchronization with Event

- The Event synchronization primitive acts as a simple communicator between threads.
- They are based on an internal flag which threads can set() or clear().
- Other threads can wait() for the internal flag to be set().
- The wait() method blocks until the flag becomes true.

Following snippet demonstrates how Events can be used to trigger actions.
"""
import random
import time
from threading import Event, Thread

event = Event()


def waiter(event, nloops):
    for i in range(nloops):
        print("% s. Waiting for the flag to be set." % (i + 1))
        event.wait()  # Blocks until the flag becomes true.
        print("Wait complete at: ", time.ctime())
        event.clear()  # Resets the flag.
        print()


def setter(event, nloops):
    for _ in range(nloops):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.
        event.set()


threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")
