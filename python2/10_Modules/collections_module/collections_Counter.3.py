import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print 'C1:', c1
print 'C2:', c2

print 'Combined counts:'
print c1 + c2

print 'Subtraction:'
print c1 - c2

print 'Intersection (taking positive minimums):'
print c1 & c2

print 'Union (taking maximums):'
print c1 | c2
