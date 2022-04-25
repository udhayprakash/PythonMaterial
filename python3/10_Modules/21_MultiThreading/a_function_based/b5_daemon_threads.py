"""
Purpose:
    enumerate() function returns a list of active Thread instances in a program.
        - return a list of all Thread objects currently active.
        - The list includes daemonic threads and dummy thread objects
          created by current_thread().
        - It excludes terminated threads and threads that have not yet been started.
        - However, the main thread is always part of the result, even when terminated.
"""

import logging
import random
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%d-%b-%Y %I:%M:%S %p",
    format="%(asctime)s (%(threadName)-10s) %(message)s",
)


def student():
    """thread student function"""
    pause = 5  # random.randint(1, 5)
    logging.debug("sleeping %s", pause)
    time.sleep(pause)
    logging.debug("ending")


t1 = threading.Thread(target=student, name="ordinary")
t1.start()

# Starting Daemon threads
# NOTE: If the main thread is killed, daemon thread will be killed as well.
t2 = threading.Thread(target=student, name="daemon1")
t2.daemon = True
t2.start()

t3 = threading.Thread(target=student, name="daemon2", daemon=True)
t3.start()

for i in range(3, 10):
    t = threading.Thread(target=student, name=f"daemon{i}", daemon=True)
    t.start()


main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug("joining %s", t.name)
    t.join()


"""
NOTE:
    - The threads which are always going to run in the background that provides
    supports to main or non-daemon threads, those background executing threads
    are considered as Daemon Threads.
    - The Daemon Thread does not block the main thread from exiting and continues
    to run in the background.
"""
