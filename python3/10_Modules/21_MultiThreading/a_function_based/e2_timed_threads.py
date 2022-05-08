import time
from threading import Thread


def timer(name, delay, repeat):
    print("Timer: " + name + " Started")

    while repeat > 0:
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + "Completed")


thread1 = Thread(target=timer, args=("Timer1", 1, 5))
thread2 = Thread(target=timer, args=("Timer2", 2, 5))
thread1.start()
thread2.start()

thread1.join(timeout=None)  # it will wait until it completes
thread2.join(timeout=3)  # waits until 3 seconds

# As join() always returns None, you must call is_alive() after join() to decide
# whether a timeout happened – if the thread is still alive, the join() call timed out.

print("thread1.is_alive()=", thread1.is_alive())
print("thread2.is_alive()=", thread2.is_alive())

print("End =================")
