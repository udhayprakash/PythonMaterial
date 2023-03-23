"""
Purpose: Using Locks as context manager
"""
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug("Lock acquired directly")
    finally:
        lock.release()


def worker_with(lock):
    with lock:
        logging.debug("Lock acquired via with")


lock = threading.Lock()
nw = threading.Thread(target=worker_no_with, args=(lock,))
w = threading.Thread(target=worker_with, args=(lock,))

nw.start()
w.start()
