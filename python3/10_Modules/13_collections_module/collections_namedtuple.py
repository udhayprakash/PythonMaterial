bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'female')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [ bob, jane ]:
    print('%s is a %d year old %s' % p)

print('-' * 30) 
import collections

Person = collections.namedtuple('Person', 'name age gender')

print('Type of Person:', type(Person))

bob = Person(name='Bob', age=30, gender='male')
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29, gender='female')
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [ bob, jane ]:
    print('%s is a %d year old %s' % p)
    
print('-' * 30) 
try:
    collections.namedtuple('Person', 'name class age gender')
except ValueError as err:
    print(err)

try:
    collections.namedtuple('Person', 'name age gender age')
except ValueError as err:
    print(err)

print('-' * 30) 

with_class = collections.namedtuple('Person', 'name class age gender', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age gender age', rename=True)
print(two_ages._fields)


print('-' * 30) 
colors=collections.namedtuple('colors','r g b')
red=colors(r=255,g=0,b=0)

print('''red.r={} red.g={} red.b={}
                    '''.format(red.r, red.g, red.b))

print("getattr(red,'r')", getattr(red,'r'))
print('red[0]', red[0])

print(red._asdict()) # namedtuple into dictionary

#Iterable to namedtuple
print(colors._make(['1','2','3'])) 

# dictionary to namedtuple
print(colors(**{'r':255,'g':0,'b':0}))

# To check the fields belonging to a namedtuple
print(red._fields)

# namedtuples are immtuable, but to change a value in it 
print(red._replace(g=3))