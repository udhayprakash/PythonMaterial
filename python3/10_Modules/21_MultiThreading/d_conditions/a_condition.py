"""
Purpose: Synchronization using Condition object

- A Condition object is simply a more advanced version of the Event object.
- It too acts as a communicator between threads and can be used to notify()
  other threads about a change in the state of the program.
- Ex: it can be used to signal the availability of a resource for consumption.
- Other threads must also acquire() the condition (and thus its related lock)
  before wait()ing for the condition to be satisfied.
- Also, a thread should release() a Condition once it has completed the related
  actions, so that other threads can acquire the condition for their purposes.

- Also, conditions are useful, when developing a streaming API which notifies
  a waiting client once a piece of data is available.

Following code demonstrates the implementation of another simple
producer-consumer problem with the help of the Condition object.
"""
import random
import time
from threading import Condition, Thread

# 'condition' variable will be used to represent the availability of a produced item.
condition = Condition()

# shared object
values = []


def producer(ntimes):
    for i in range(ntimes):
        val = f"Producer- { random.randint(1, 10)}"
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.

        condition.acquire()
        values.append(val)  # writing on shared object

        condition.notify()  # Notifies the consumer about the availability.
        print(val)
        condition.release()


def consumer(ntimes):
    for i in range(ntimes):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.

        condition.acquire()
        condition.wait()  # Blocks until an item is available for consumption.
        print("Received - ", values.pop())
        condition.release()


threads = []
for func in (producer, consumer):
    t = Thread(target=func, args=(5,))
    t.start()  # Starts the thread.
    threads.append(t)

for thread in threads:
    """Waits for the threads to complete before moving on with the main script."""
    thread.join()

print("All done.")
