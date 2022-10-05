import signal
import time


def handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise OSError("timeout exceeded!")


def long_function():
    time.sleep(10)


# Set the signal handler and a 1-second alarm
old_handler = signal.signal(signal.SIGALRM, handler)  # DOESNT WORK IN WINDOWS
signal.alarm(1)
# This sleeps for longer than the alarm
start = time.time()
try:
    long_function()
except OSError as e:
    duration = time.time() - start
    print("Duration: %.2f" % duration)
    raise
finally:
    signal.signal(signal.SIGALRM, old_handler)
    signal.alarm(0)  # Disable the alarm

# ref - https://anonbadger.wordpress.com/2018/12/15/python-signal-handlers-and-exceptions/
