"""
Purpose: Timer in threads
    A Timer starts its work after a delay,
    and can be canceled at any point within that delay time period.

"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)


def delayed():
    logging.debug("Thread program still running")


t1 = threading.Timer(3, delayed)
t1.name = "Timer 1"
t2 = threading.Timer(3, delayed)
t2.name = "Timer 2"

logging.debug("Starting thread timers")
t1.start()
t2.start()

logging.debug("We are waiting before canceling %s", t2.name)
time.sleep(2)
logging.debug("Now canceling %s", t2.name)
t2.cancel()
