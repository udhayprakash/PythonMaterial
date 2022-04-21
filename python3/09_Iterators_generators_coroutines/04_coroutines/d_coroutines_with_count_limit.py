#!/usr/bin/python3
"""
Purpose:  finite reception
"""
def my_coroutine(count=5):
    for i in range(count):
        received = yield 1234   # values will be received here
        print(f'Received :{received}')


# Step 1: creating the generator
it = my_coroutine(5)

# Step 2: Prime the coroutine
print(f'{next(it) =}')

# Step 3: sending values to coroutine
it.send('First')
it.send('Second')
it.send('third')

for i in range(9):
    it.send(i)

# Step 4: close the coroutine
it.close()

try:
    it.send('fourth')
except StopIteration:
    print('coroutine is closed. Cant send any value')
