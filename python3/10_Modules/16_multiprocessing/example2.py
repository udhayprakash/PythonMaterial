import multiprocessing as mp
import collections

Msg = collections.namedtuple('Msg', ['event', 'args'])


class BaseProcess(mp.Process):
    """A process backed by an internal queue for simple one-way message passing.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = mp.Queue()

    def send(self, event, *args):
        """Puts the event and args as a `Msg` on the queue
        """
        msg = Msg(event, args)
        self.queue.put(msg)

    def dispatch(self, msg):
        event, args = msg

        handler = getattr(self, "do_%s" % event, None)
        if not handler:
            raise NotImplementedError(
                "Process has no handler for [%s]" % event)

        handler(*args)

    def run(self):
        while True:
            msg = self.queue.get()
            self.dispatch(msg)

# usage


class MyProcess(BaseProcess):
    def do_helloworld(self, arg1, arg2):
        print(arg1, arg2)


if __name__ == "__main__":
    process = MyProcess()
    process.start()
    process.send('helloworld', 'hello', 'world')
