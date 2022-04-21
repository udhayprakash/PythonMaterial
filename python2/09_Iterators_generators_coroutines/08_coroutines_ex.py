from __future__ import print_function

def highlightVowels():
    while True:
        myString = yield
        print ''.join([ch.upper() if ch.lower() in ['a', 'e', 'i', 'o', 'u'] else ch for ch in myString])

hV = highlightVowels()

next(hV)  # coroutine starts
print hV.send('Python Programming Language')
print hV.send('Today is a good day')

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it) # Start the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
