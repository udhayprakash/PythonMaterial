import collections

c = collections.Counter()

with open(r"C:\Python311\LICENSE.txt", "rt") as f:
    # print(f.read())
    for line in f:
        # print(line.rstrip().lower())
        c.update(line.rstrip().lower())

print("Dict    :", c)

print("Most common:")
for letter, count in c.most_common(5):
    print("%s: %7d" % (letter, count))

# assignment: Try to get the 4 least common characters
