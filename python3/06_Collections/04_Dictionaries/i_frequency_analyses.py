#!/usr/bin/python
"""
Purpose: Test Frequency Analyses
"""
sentence = '''Python is a wonderful language. 
we can solve any 
computational problem with this language'''

# Character frequency analyses
# Method 1
frequency = {}
for each_char in sentence:
    # print(each_char)
    try:
        frequency[each_char] = frequency[each_char] + 1
    except KeyError as ex:
        # print('No such key', ex)
        frequency[each_char] = 1

print(frequency)

# Method 2
frequency = {}
for each_char in sentence:
    frequency.setdefault(each_char, 0) # creates key with value 0, if key is not present
    frequency[each_char] = frequency[each_char] + 1

print(frequency)

# Method 3
frequency = {}
for each_char in sentence:
    if each_char in frequency:
        # key is present 
        # frequency[each_char] = frequency[each_char] + 1
        frequency[each_char] += 1
    else:
        # key not present 
        frequency[each_char] = 0

print(frequency)


# Method 4
frequency = {}
for each_char in sentence:
    # frequency[each_char] = frequency.get(each_char) + 1  # 'NoneType' and 'int'
    frequency[each_char] = frequency.get(each_char, 0) + 1 

print(frequency)


# -----------------------------
print()
print(f"{sorted('abacus')      =}")
print(f"{sorted('322321')      =}")
print(f"{sorted([23,43,-2, 1]) =}")
print(f"{sorted([23,43,-2, 1], reverse=True) =}")

print()
frequency1 = {'a': 3, 'b': 2, 'c': 2, 'd': 1}
print(f'{frequency1                 =}')
print(f'{sorted(frequency1)         =}')
print(f'{sorted(frequency1.keys())  =}')
print(f'{sorted(frequency1.values())=}')

print()
print(f'{sorted(frequency1.items()) =}') 
# default - sort by 0th value in pair

print(f'{sorted(frequency1.items(), reverse=True) =}') 

print()
print(f'{sorted(frequency1.items()) =}') 
print(f'{sorted(frequency1.items(), key=lambda x:x[0]) =}') # sort by key
print(f'{sorted(frequency1.items(), key=lambda x:x[0], reverse=True) =}') # sort by key

print(f'{sorted(frequency1.items(), key=lambda x:x[1]) =}') # sort by value
print(f'{sorted(frequency1.items(), key=lambda x:x[1], reverse=True) =}') # sort by value


frequency1_result = dict(sorted(frequency1.items(), key=lambda x:x[1], reverse=True))
print(frequency1_result)
print(frequency1_result.keys())
print('Top 3 chars in frequecny are', list(frequency1_result.keys())[:3])


# Assignment 
# In character frequency analyses, try to get top 5 occurring characters
sorted(frequency.items, key=lambda x:x[1])[-5:]
'''
Assignment
==========
choose a large sentence greater than 150 words and perform the following
1) character frequency analyses
    a) case sensitive
        {
            'P': 1,
            'y': 2,
            't : 5
            ....
        }
    b) case insensitive
        {
            'p': 2,
            'y': 2,
            't : 5
            .....
        }
        HINT: str.lower()
2) word frequency analyses
    a) case sensitive 
    b) case insensitive
    HINT: str.split()

3) cleansed_words frequency analyses 
        HINT: string module -> string.punctuation
    a) case sensitive 
    b) case insensitive

    Are you coming?  --> ['Are', 'you', 'coming']

'''