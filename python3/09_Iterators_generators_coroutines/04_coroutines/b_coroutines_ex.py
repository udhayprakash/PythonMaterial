
def repeater():
    while True:
        received = yield 'Uhdya'
        print('Echo:', received)

rp = repeater()

print(next(rp)) # Start the coroutine
rp.send('Aruna')
rp.send('Akram')
rp.send('Jaya')
rp.send('World')
rp.close()

rp.send('Hello')