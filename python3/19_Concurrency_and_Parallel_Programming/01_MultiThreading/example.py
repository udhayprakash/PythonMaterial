import threading

x = 0


def increment():
    global x
    x += 1


def threadTask():
    for _ in range(50):
        increment()


def main():
    global x
    x = 0

    p1 = threading.Thread(target=threadTask)
    p2 = threading.Thread(target=threadTask)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    for i in range(5):
        main()
        print(f"x = {i} -> iteration {x}")


# ======================================
import inspect
import threading

for name, obj in inspect.getmembers(threading):
    if inspect.issubclass(obj):
        print(name)
