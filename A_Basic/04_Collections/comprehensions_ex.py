
######################################
for i in xrange(2,9):
    print i 

print [i for i in xrange(2,9)]

#########################################
new = []
for ch in 'Mangalyan':
    new.append(ch)
print new

print [ch for ch in 'Mangalyan']

my_variable = [ch for ch in 'Mangalyan']
print "type(my_variable)", type(my_variable)

my_variable = (ch for ch in 'Mangalyan')
print "type(my_variable)", type(my_variable)

my_variable = {ch for ch in 'Mangalyan'}
print "type(my_variable)", type(my_variable)

my_variable = {ch:ord(ch)+1 for ch in 'Mangalyan'}
print "type(my_variable)", type(my_variable)
print 'my_variable', my_variable
