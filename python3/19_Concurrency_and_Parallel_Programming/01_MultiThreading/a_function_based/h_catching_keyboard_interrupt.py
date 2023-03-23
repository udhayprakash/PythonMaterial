import threading
import time


def timed_output(name, delay, run_event):
    while run_event.is_set():
        time.sleep(delay)
        print(name, ": New Message!")


def main():
    run_event = threading.Event()
    run_event.set()
    d1 = 1
    t1 = threading.Thread(target=timed_output, args=("bob", d1, run_event))

    d2 = 2
    t2 = threading.Thread(target=timed_output, args=("paul", d2, run_event))

    t1.start()
    time.sleep(0.5)
    t2.start()

    try:
        while 1:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("attempting to close threads. Max wait =", max(d1, d2))
        run_event.clear()
        t1.join()
        t2.join()
        print("threads successfully closed")


if __name__ == "__main__":
    main()
