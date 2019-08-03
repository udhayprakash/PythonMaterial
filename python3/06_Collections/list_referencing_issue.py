'''
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0]
[]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
>>> # Note that items in the sequence s are not copied; they are referenced multiple times.
...
>>>
>>> # solution
...
>>> lists = [[] for i in range(3)]
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [], []]
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
'''