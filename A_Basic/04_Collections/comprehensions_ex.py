new_list = []
for i in xrange(2,9):
    new_list.append(i)

print new_list 

print [i for i in xrange(2,9)]

##########
new_list = []
for i in xrange(2,9):
    if i %2 != 0:
        new_list.append(i)
print new_list 

print [i for i in xrange(2,9) if i %2 != 0]
###################
new_list = []
for i in xrange(2,9):
    if i%2 != 0:
        new_list.append('odd')
    else:
        new_list.append('even')
print new_list

print ['odd' if i%2 != 0 else 'even' for i in xrange(2,9)]
# #########################################

my_variable = [ch for ch in 'Mangalyan']
print type(my_variable), my_variable

my_variable = (ch for ch in 'Mangalyan')
print type(my_variable), my_variable

my_variable = {ch for ch in 'Mangalyan'}
print type(my_variable), my_variable

my_variable = {ch:ord(ch)+1 for ch in 'Mangalyan'}
print "type(my_variable)", type(my_variable)
print type(my_variable), my_variable
