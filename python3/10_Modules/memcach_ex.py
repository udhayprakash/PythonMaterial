#!/usr/bin/python
# Using memcached to cache expensive results.
# pip install python-memcached

import memcache, random, time, timeit

# starting the memcache client
mc = memcache.Client(['127.0.0.1:11211'])

def compute_square(n):
    value = mc.get('sq:%d' % n)
    if value is None:
        time.sleep(0.001) # pretend that computing a square is expensive
        value = n * n
        mc.set('sq:%d' % n, value)
    return value

def make_request():
    compute_square(random.randint(0, 5000))

print('Ten successive runs:')
for i in range(1, 11):
    print('%.2fs' % timeit.timeit(make_request, number=2000))

print()