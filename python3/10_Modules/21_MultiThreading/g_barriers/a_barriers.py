"""
Purpose: Synchronization with Barriers
- for use by a fixed number of threads that need to wait for each other.
- Each thread tries to pass a barrier by calling the wait() method, which will
  block until all of threads have made that call.
  As soon as that happens, the threads are released simultaneously.
- The barrier can be reused any number of times for the same number of threads.

- UseCase: synchronizing a server and a client
    — as the server has to wait for the client after initializing itself.

Following snippet demonstrates the use of Barriers.
"""

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ["Ramesh", "Ganesh", "Mahesh", "Suresh"]


def player():
    name = names.pop()
    sleep(randrange(2, 10))
    print("%s reached the barrier at: %s" % (name, ctime()))
    b.wait()


threads = []
print("Race starts now…")

for i in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()

"""
Following loop enables waiting for the threads to complete before moving on with the main script.
"""

for thread in threads:
    thread.join()
print()

print("Race over!")
