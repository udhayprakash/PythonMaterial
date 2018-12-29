# for (int a = 0; a < 10 ; a ++)

language = "python programming"

# iterating over a string  
for i in language:
    print i,        
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

for loop_count, number in enumerate(numbers):
    print loop_count, '-->', number

print '-'*20
######################
for index, number in enumerate(range(-100,100000, 3)): 
    # print '\n', i,
    # if not number:
    #     print 'number', number
    #     continue
    print '\r', index/float(number), '% completed',
