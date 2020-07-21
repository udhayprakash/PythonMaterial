integers = list(range(8))
squared = (i * i for i in integers)
negated = (-i for i in squared)

print(type(negated), negated)
for each in negated:
    print(each)

squared = (i * i for i in integers)
negated = (-i for i in squared)

print(list(negated))
