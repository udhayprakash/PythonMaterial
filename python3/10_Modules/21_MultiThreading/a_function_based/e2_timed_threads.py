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

print("End =================")
