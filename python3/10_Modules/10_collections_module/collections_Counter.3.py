import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('c1:', c1)
print('c2:', c2)

print('Combined counts:')
print(c1 + c2)

print('Subtraction:')
print(c1 - c2)

print('Intersection (taking positive minimums):')
print(c1 & c2)

print('Union (taking maximums):')
print(c1 | c2)