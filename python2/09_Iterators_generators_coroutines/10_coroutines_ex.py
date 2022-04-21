from __future__ import print_function

def my_coroutine():
    while True:
        received = yield
        print('Received:', received)

it = my_coroutine()
next(it)             # Prime the coroutine
it.send('First')
it.send('Second')
