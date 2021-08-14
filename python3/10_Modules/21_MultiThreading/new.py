import threading


class Worker(threading.Thread):
    # Our workers constructor, note the super() method which is vital if we want this
    # to function properly
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(10):
           print(i)


def main():
    # This initializes ''thread1'' as an instance of our Worker Thread
    thread1 = Worker()
    # This is the code needed to run our newly created thread
    thread1.start()

if __name__ == "__main__":
    main()
