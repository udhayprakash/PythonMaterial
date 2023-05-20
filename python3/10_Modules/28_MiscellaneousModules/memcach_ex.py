#!/usr/bin/python
"""
Purpose: Using memcached to cache expensive results.

    pip install -U python-memcached --user
"""

import random
import time
import timeit

import memcache

# starting the memcache client
mc = memcache.Client(["127.0.0.1:11211"])


def is_request_allowed(ip_address):
    # Generate a unique cache key based on the IP address and current time
    cache_key = f"rate_limit:{ip_address}"
    # Increment the value stored in the cache for the given key
    count = mc.incr(cache_key, 1)
    if count == 1:
        # Set an expiration time of 1 minute for the cache key
        mc.expire(cache_key, 60)
    # Check if the request count exceeds the allowed limit
    if count > 100:
        return False
    return True


def compute_square(n):
    value = mc.get("sq:%d" % n)
    if value is None:
        time.sleep(0.001)  # pretend that computing a square is expensive
        value = n * n
        mc.set("sq:%d" % n, value)
    return value


def make_request():
    compute_square(random.randint(0, 5000))


print("Ten successive runs:")
for i in range(1, 11):
    print("%.2fs" % timeit.timeit(make_request, number=2000))


"""
Set a value in memcached: client.set('key', 'value')
Get a value from memcached: value = client.get('key')
Check if a key exists: exists = client.get('key') is not None
Delete a key from memcached: client.delete('key')
Increment a numeric value: client.incr('counter', 1)
Decrement a numeric value: client.decr('counter', 1)
Add a key-value pair only if the key doesn't exist: client.add('key', 'value')
Replace the value of an existing key: client.replace('key', 'new_value')
Append data to the value of an existing key: client.append('key', 'additional_data')
Prepend data to the value of an existing key: client.prepend('key', 'prefix_data')
Store a key-value pair with an expiration time (in seconds): client.set('key', 'value', time=3600)
Store multiple key-value pairs: client.set_multi({'key1': 'value1', 'key2': 'value2'})
Get multiple values using a list of keys: values = client.get_multi(['key1', 'key2'])
Check if a key has expired: expired = client.get('key') is None
Flush all keys in memcached: client.flush_all()
Get the statistics of the memcached server: stats = client.get_stats()
Get the value and CAS token of a key: value, cas_token = client.gets('key')
Check and set a key if its CAS token matches: client.cas('key', 'new_value', cas_token)
Set a value with a specific flag: client.set('key', 'value', flags=1)
Get the flag value of a key: flags = client.get('key', get_flags=True)
Touch a key to reset its expiration time: client.touch('key', time=3600)
Store a key-value pair with a specific namespace: client.set('namespace:key', 'value')
Get all keys stored in memcached: keys = client.get_stats('items')[0]['items']
Get the version of the memcached server: version = client.get_stats('version')[0]['version']
Enable or disable the binary protocol: client.set_protocol_version(1) (binary) or client.set_protocol_version(0) (ASCII)
Enable or disable the no-reply feature: client.behaviors['noreply'] = True or client.behaviors['noreply'] = False
Set a timeout for network operations (in seconds): client.socket_timeout = 5
Close the connection to the memcached server: client.disconnect_all()
"""
