"""
Purpose: Synchronization using SemaPhores

    - Semaphores are simply advanced counters.
    - An acquire() call to a semaphore will block only after a number of threads have
      acquire()ed it.
    - The associated counter decreases per acquire() call, and increases per release() call.
    - A ValueError will occur if release() calls try to increment the counter beyond
      it's assigned maximum value (which is the number of threads that can acquire()
      the semaphore before blocking occurs).
    - Semaphores are typically used for limiting a resource, like limiting a server to
      handle only 10 clients at a time. In such a case, multiple thread connections compete
      for a limited resource.
Following code demonstrates the use of semaphores in a simple producer-consumer problem.
"""
import random
import time
from threading import BoundedSemaphore, Thread

max_items = 5

"""
Consider 'container' as a container, of course, with a capacity of 5
items. Defaults to 1 item if 'max_items' is passed.
"""
container = BoundedSemaphore(max_items)


def producer(nloops):
    for _ in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, skipping.")


def consumer(nloops):
    for _ in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        """
        In the following if statement we disable the default
        blocking behaviour by passing False for the blocking flag.
        """
        if container.acquire(False):
            print("Consumed an item.")
        else:
            print("Empty, skipping.")


threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(
    Thread(target=consumer, args=(random.randrange(nloops, nloops + max_items + 2),))
)


# Starts all the threads.
for thread in threads:
    thread.start()


# Waits for threads to complete before moving on with the main script.
for thread in threads:
    thread.join()


print("All done.")
