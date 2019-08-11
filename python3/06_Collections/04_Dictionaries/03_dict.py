
sentence = '''Python is a wonderful language. 
we can solve any 
computational problem with this language'''


frequency = {}
for ech_ch in sentence:
    frequency[ech_ch] = frequency.get(ech_ch, 0) + 1

print(frequency)

# print(sorted(frequency))
# print(sorted(frequency.keys()))
# print(sorted(frequency.values()))

# print('\n', frequency.items())
# print('\n', sorted(frequency.items()))
# print('\n', sorted(frequency.items(), key=lambda x:x[0]))
# print('\n', sorted(frequency.items(), key=lambda x:x[1]))
# print('\n', sorted(frequency.items(), key=lambda x:x[1], reverse=True))

top_three_chars = sorted(frequency.items(), key=lambda x:x[1], reverse=True)[:6]
print(top_three_chars)


top_chars_in_asc = sorted(frequency.items(), key=lambda x:[-x[1], x[0]], reverse=True)[:6]
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






HINT: setdefault


'''