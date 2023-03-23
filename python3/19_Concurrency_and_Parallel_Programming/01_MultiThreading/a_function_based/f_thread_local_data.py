"""
Purpose: To show thread specific data
"""
import logging
import random
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-18s) %(message)s",
)


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.error("No value yet")
    else:
        logging.debug(f"value={val}")


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


local_data = threading.local()
show_value(local_data)

local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

# threading.local() is not a singleton.
# we can use more of them per thread. It is not one storage.
local_data1 = threading.local()
show_value(local_data)
