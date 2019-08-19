
def my_coroutine():
    while True:
        received = yield 12312
        print('Received:', received)

# creating the generator
it = my_coroutine()

print(next(it))  # Prime the coroutine


it.send('First')
it.send('Second')
it.send('third')

for i in range(9):
    it.send(i)

it.close()

# it.send('fouth')  # StopIteration
