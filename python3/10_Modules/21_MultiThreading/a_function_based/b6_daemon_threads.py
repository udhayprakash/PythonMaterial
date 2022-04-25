# threading daemon

import logging
import threading
import time


def daemon():
    logging.debug("Starting")
    time.sleep(2)
    logging.debug("Exiting")


def non_daemon():
    logging.debug("Starting")
    # time.sleep(3)  # observe difference
    logging.debug("Exiting")


logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)

d = threading.Thread(name="daemon", target=daemon, daemon=True)

t = threading.Thread(name="non-daemon", target=non_daemon)

d.start()
t.start()
