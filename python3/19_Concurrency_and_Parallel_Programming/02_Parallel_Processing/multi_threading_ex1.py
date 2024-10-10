import time
from threading import Thread
import secrets


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        amount = secrets.SystemRandom().randint(3, 15)
        time.sleep(amount)
        msg = "{} is running".format(self.name)
        print(msg)


def create_threads():
    for i in range(5):
        name = "Thread {}".format(i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
