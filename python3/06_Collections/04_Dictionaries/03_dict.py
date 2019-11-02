sentence = '''Python is a wonderful language. 
we can solve any 
computational problem with this language'''

# # Method 1
# frequency = {}
# for each_ch in sentence:
#     if frequency.get(each_ch): 
#         # If key already exists
#         frequency[each_ch] += 1
#     else:
#         # If key not present
#         frequency[each_ch] = 1

# print(frequency)


# # Method 2
# frequency = {}
# for each_ch in sentence:
#     frequency[each_ch] = frequency.get(each_ch, 0) + 1

# print(frequency)

# Method 3
frequency = {}
for each_ch in sentence:
    frequency.setdefault(each_ch, 0)
    frequency[each_ch] += 1

print(frequency)

print()
frequency1 = {'a': 3, 'b': 2, 'c': 2, 'd': 1}
print(sorted(frequency1))
print(sorted(frequency1.keys()))
print(sorted(frequency1.values()))

print('\n', frequency1.items())
print('\n', sorted(frequency1.items()))
print('\n', sorted(frequency1.items(), key=lambda x:x[0]))
print('\n', sorted(frequency1.items(), key=lambda x:x[1]))
print('\n', sorted(frequency1.items(), key=lambda x:x[1], reverse=True))

top_three_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]
print(top_three_chars)

top_chars_in_asc = sorted(frequency.items(), key=lambda x: [-x[1], x[0]])[:3]
print(top_chars_in_asc)

'''


character frequency analyses  
    - case sensitive
        {
            'P': 1,
            'y': 2,
            't : 5
            ....
        }
    - case insensitive
        {
            'p': 2,
            'y': 2,
            't : 5
            .....
        }
word frequency analyses  
