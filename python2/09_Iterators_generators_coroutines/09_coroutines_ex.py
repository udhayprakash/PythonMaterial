from __future__ import print_function

def repeater():
    while True:
        received = yield
        print('Echo:', received)

rp = repeater()

next(rp) # Start the coroutine
rp.send('Hello')
rp.send('World')