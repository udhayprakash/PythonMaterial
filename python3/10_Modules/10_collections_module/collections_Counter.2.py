import collections

c = collections.Counter()

with open(r'C:\Python27\README.rst', 'rt') as f:
    # print(f.read())
    for line in f:
        # print(line.rstrip().lower())
        c.update(line.rstrip().lower())

print('Dict    :', c)

print('Most common:')
for letter, count in c.most_common(5):
    print('%s: %7d' % (letter, count))
