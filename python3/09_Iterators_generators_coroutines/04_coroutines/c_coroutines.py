#!/usr/bin/python
"""
Purpose: 
"""
def my_coroutine():
    while True:
        received = yield 1234
        print(f'Received :{received}')

# Step 1: creating the generator
it = my_coroutine()

# Step 2: Prime the coroutine
print(next(it))  

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