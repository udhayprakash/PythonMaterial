#!/usr/bin/python3
"""
Purpose: Heap - will store data in sorted order, for each modification

Heaps are concrete data structures,
whereas priority queues are abstract data structures.

An abstract data structure determines the interface,
while a concrete data structure defines the implementation.

Heaps are commonly used to implement priority queues.

"""

import datetime
import heapq

heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create tests'))

# pops smallest
heapq.heappop(heap)  # (1, 'write spec')

# displays n largest values without popping
heapq.nlargest(2, heap)  # [(7, 'release product'), (5, 'write code')]

# displays n smallest values without popping
heapq.nsmallest(2, heap)  # [(3, 'create tests'), (5, 'write code')]

# =============================================
heap = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(heap)  # converts a list to heap
print(heap)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


# ----------------------------


def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details


fast_email = email(datetime.timedelta(minutes=15), 'fast email')
slow_email = email(datetime.timedelta(minutes=40), 'slow email')

unified = heapq.merge(fast_email, slow_email)
print(unified)

# ==========================================================
# Heaps can also help identify the top n or bottom n things.

results = """\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""
top_3 = heapq.nsmallest(
    3, results.splitlines(), key=lambda x: float(x.split()[-1])
)
print('\n'.join(top_3))
