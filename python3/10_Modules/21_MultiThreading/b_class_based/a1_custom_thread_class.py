#!/usr/bin/python


import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-20s) %(message)s",
)


class MyThread(threading.Thread):
    def run(self):
        logging.debug("This thread is running")
        return


for x in range(5):
    z = MyThread()
    z.start()
    time.sleep(1)
