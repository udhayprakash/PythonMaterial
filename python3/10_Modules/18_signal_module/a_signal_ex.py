#!/usr/bin/python
"""
Purpose:
"""
import os
import signal
import sys
import time

print(dir(signal))


def receive_signal(signum, stack):
    print("Received:", signum)


if not sys.platform == "win32":
    # Register signal handlers
    signal.signal(signal.SIGUSR1, receive_signal)
    signal.signal(signal.SIGUSR2, receive_signal)

    # Print the process ID so it can be used with 'kill'
    # to send this program signals.
    print("My PID is:", os.getpid())

    while True:
        print("Waiting...")
        time.sleep(3)
