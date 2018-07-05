n = int(raw_input('').strip())
strings = []
if 1 <= n <= 1000:
    for i in xrange(n):
        inputString = raw_input('')
        if 1 <= len(inputString) <= 20:
            strings.append(inputString)
                
q = int(raw_input('').strip())
strings1 = []
if 1 <= q <= 1000:
    for i in xrange(q):
        inputString = raw_input('')
        if 1 <= len(inputString) <= 20:
            strings1.append(inputString)

for word in strings1:
    print strings.count(word)