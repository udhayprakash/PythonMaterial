
def repeater():
    while True:
        received = yield 'Uhdya'
        print('Echo:', received)

rp = repeater()

print(next(rp)) # Start the coroutine
rp.send('Hello')
rp.send('World')