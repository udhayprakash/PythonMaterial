#!/usr/bin/python


import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print(f"{self.name} started!")  # Thread-x started
        time.sleep(1)
        print(f"{self.name} finished!")  # Thread-x finished


def Main():
    for x in range(4):
        # Instantiate a thread and pass a unique ID to it
        mythread = MyThread(name="Thread-{}".format(x + 1))
        mythread.start()
        time.sleep(1)


if __name__ == "__main__":
    Main()
