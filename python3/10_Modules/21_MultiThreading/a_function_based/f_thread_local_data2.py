"""
Purpose: Showing thread specific data
"""
import logging
import random
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-20s) %(message)s",
)


def show_value(data):
    logging.debug("show_value - start")
    try:
        val = data.value
    except AttributeError:
        logging.error("No value yet")
    else:
        logging.debug("value=%s", val)


def worker(data):
    logging.debug("worker - start")
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


class MyLocal(threading.local):
    def __init__(self, value):
        logging.debug("Initializing %r", self)
        self.value = value


local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
    t.join()

# OUTPUT
# (MainThread          ) Initializing <__main__.MyLocal object at 0x0000019F4082A380>
# (MainThread          ) show_value - start
# (MainThread          ) value=1000

# (Thread-1 (worker)   ) worker - start
# (Thread-1 (worker)   ) show_value - start
# (Thread-1 (worker)   ) Initializing <__main__.MyLocal object at 0x0000019F4082A380>
# (Thread-1 (worker)   ) value=1000
# (Thread-1 (worker)   ) show_value - start
# (Thread-1 (worker)   ) value=7

# (Thread-2 (worker)   ) worker - start
# (Thread-2 (worker)   ) show_value - start
# (Thread-2 (worker)   ) Initializing <__main__.MyLocal object at 0x0000019F4082A380>
# (Thread-2 (worker)   ) value=1000
# (Thread-2 (worker)   ) show_value - start
# (Thread-2 (worker)   ) value=38
