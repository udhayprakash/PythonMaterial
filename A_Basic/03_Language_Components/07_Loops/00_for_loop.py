# for (int a = 0; a < 10 ; a ++)

language = "python programming"

# iterating over a string  
for ch in language:
    print ch,
print

# enumerate - gives the loop index
# iterating over a string
for index, ch in enumerate(language):
    # print index, ch
    # print "character at %d position is %s"%(index, ch)
    print "character at %2d position is %1s" % (index, ch)
print
#
numbers = [12, 34, 5, 6, 7, 99, 888]

# Iterating over a list of elements
for number in numbers:
    print number,
print

for index, number in enumerate(numbers):
    print index, '-->', number



