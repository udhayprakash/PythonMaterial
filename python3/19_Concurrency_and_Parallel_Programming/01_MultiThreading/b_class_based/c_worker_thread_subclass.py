#!/usr/bin/python3
import threading
import time
import secrets


class WorkerThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.id = id(self)

    def run(self):
        """
        Run the thread
        """
        worker(self.name, self.id)


def worker(name: str, instance_id: int) -> None:
    print(f"Started worker {name} - {instance_id}")
    worker_time = secrets.choice(range(1, 5))
    time.sleep(worker_time)
    print(f"{name} - {instance_id} worker finished in " f"{worker_time} seconds")


if __name__ == "__main__":
    for i in range(5):
        thread = WorkerThread(name=f"computer_{i}")
        thread.start()
