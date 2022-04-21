import itertools

for i in itertools.count(7):
    if i>14:
        break
    print(i)


print itertools.count(7)

# # continuously propagates integers from 0
# for i in itertools.count():
#     print(i)


# itertools.cycle() - infinitely iterates over a python
# iterables, unless we explicitly break out of the loop.

c=0
for i in itertools.cycle(['Head','Tail']):
    if c>7:
        break
    print(i)
    c+=1


# itertools.repeat() - This one repeats an object infinitely
# unless explicitly broken out of.

c=0
for i in itertools.repeat([1,2,3]):
    if c>7:
        break
    print(i)
    c+=1

# We can also specify the number of times we want
# it to repeat, as a second argument.

for i in itertools.repeat([1,2,3],4):
                print(i)
