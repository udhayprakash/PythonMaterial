from collections import Counter

print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(Counter('python programming'))
print() 

print(Counter({'a':2, 'b':3, 'c':1}))

print() 
print(Counter(a=2, b=3, c=1))

print() 
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Yellow'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

print([name for name, colour in colours])
favs = Counter(name for name, colour in colours)
print(favs)
favs = Counter(colour for name, colour in colours)
print(favs)

print('-' * 30)
c = Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a':1, 'd':5})
print('Dict    :', c)

print('-' * 30) 

c = Counter('abcdaab')

for letter in 'abcde':
    print('%s : %d' % (letter, c[letter]))

print('-' * 30) 
c = Counter('extremely')
c['z'] = 0

print(c)
print(list(c.elements()))
