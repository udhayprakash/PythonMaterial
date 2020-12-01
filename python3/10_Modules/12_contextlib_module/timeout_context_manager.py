import signal
from time import sleep

class timeout:
    def __init__(self, seconds, *, timeout_message=""):
        self.seconds = int(seconds)
        self.timeout_message = timeout_message

    def _timeout_handler(self, signum, frame):
        raise TimeoutError(self.timeout_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)  # Set handler for SIGALRM
        signal.alarm(self.seconds)  # start countdown for SIGALRM to be raised

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)  # Cancel SIGALRM if it's scheduled
        return exc_type is TimeoutError  # Suppress TimeoutError


with timeout(3):
    # Some long running task...
    sleep(10)