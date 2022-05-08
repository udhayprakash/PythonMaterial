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

"""
'condition' variable will be used to represent the availability of a produced
item.
"""
condition = Condition()
box = []


def producer(box, nitems):
    for _ in range(nitems):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.
        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # Puts an item into box for consumption.
        condition.notify()  # Notifies the consumer about the availability.
        print("Produced:", num)
        condition.release()


def consumer(box, nitems):
    for _ in range(nitems):
        condition.acquire()
        condition.wait()  # Blocks until an item is available for consumption.
        print("%s: Acquired: %s" % (time.ctime(), box.pop()))
        condition.release()


threads = []
"""
'nloops' is the number of times an item will be produced and
consumed.
"""
nloops = random.randrange(3, 6)
for func in [producer, consumer]:
    threads.append(Thread(target=func, args=(box, nloops)))
    threads[-1].start()  # Starts the thread.

for thread in threads:
    """Waits for the threads to complete before moving on
    with the main script.
    """
    thread.join()

print("All done.")
