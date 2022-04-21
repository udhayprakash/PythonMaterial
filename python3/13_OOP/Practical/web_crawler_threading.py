import threading
from queue import Queue


class Parser(threading.Thread):
    def __init__(self, content_queue, url_queue):
        self.c_queue = content_queue
        self.u_queue = url_queue
        super(Parser, self).__init__()

    def run(self):
        while True:
            data = self.c_queue.get()
            # process data
            for link in links:
                self.u_queue.put(link)
            self.c_queue.task_done()


class Grabber(threading.Thread):
    def __init__(self, url_queue, content_queue):
        self.c_queue = content_queue
        self.u_queue = url_queue
        super(Grabber, self).__init__()

    def run(self):
        while True:
            next_url = self.u_queue.get()
            # data = requests.get(next_url)
            while self.c_queue.full():
                pass
            self.c_queue.put(data)
            self.u_queue.task_done()


num_threads = 4
max_size = 1000
url_queue = Queue()
content_queue = Queue(maxsize=max_size)

parsers = [Parser(content_queue, url_queue) for i in range(num_threads)]
grabbers = [Grabber(url_queue, content_queue) for i in range(num_threads)]

for thread in parsers + grabbers:
    thread.daemon = True
    thread.start()

url_queue.put("http://brett.is/")
