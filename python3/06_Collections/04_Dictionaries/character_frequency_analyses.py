#!/usr/bin/python
__author__ = 'udhay'

from pprint import pprint
sentence = "It is always seen imposible, until we attempt!"

count = {}
for character in sentence:
    count[character] = count.get(character,0) + 1

pprint(count)

# print(sorted(count))

# print(count.items())
# print(sorted(count.items()))
# print(sorted(count.items(), reverse= False))
# print(sorted(count.items(), reverse= True))

# print(sorted(count.items(), key = lambda i:i[0]))  # sorting by key
# print(sorted(count.items(), key = lambda i:i[1]))  # sorting by value


# print(sorted(count.items(), key = lambda i:i[1], reverse= True))

# top_three_chars = sorted(count.items(), key = lambda i:i[1], reverse= True)[:3]
# print(top_three_chars)  # [(' ', 7), ('t', 5), ('e', 5)]

# top_three_chars = sorted(count.items(), key = lambda x:(-x[1], x[0]))[:3]
#                                                        #DESC    ASC
# print(top_three_chars)  # [(' ', 7), ('e', 5), ('t', 5)]

# print(dict(top_three_chars))


'''
In[18]: sorted({'d': 1, 'abcd': 123, 'a': 2, 'ab': 3}.items(), key = lambda l:l[1])
Out[18]:
[('d', 1), ('a', 2), ('ab', 3), ('abcd', 123)]
In[19]: sorted({'d': 1, 'abcd': 123, 'a': 2, 'ab': 3}.items(), key = lambda l:l[0])
Out[19]:
[('a', 2), ('ab', 3), ('abcd', 123), ('d', 1)]
In[20]: sorted({'d': 1, 'abcd': 123, 'a': 2, 'ab': 3}.items(), key = lambda l:len(l[0]))
Out[20]:
[('a', 2), ('d', 1), ('ab', 3), ('abcd', 123)]
'''