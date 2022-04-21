import collections

c = collections.Counter()

with open(r'C:\Python27\LICENSE.txt', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter, count in c.most_common(5):
    print '%s: %7d' % (letter, count)
