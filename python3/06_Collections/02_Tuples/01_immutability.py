# list is a mutable object
mylist = [12, 3, 4, 6]
print(mylist[2])

mylist[2] = 4444
print(mylist)


# tuple is immutable object
mytuple = (12, 3, 4, 6)
print(mytuple[2])

# mytuple[2] = 4444  # TypeError: 'tuple' object does not support item assignment
# print mytuple

student_name = 'Rahul'
print('student_name[-1]', student_name[-1])
print('id(student_name)', id(student_name))

# student_name[-1] = 't' # TypeError:

student_name = 'Theja'  # Overwriting
print('id(student_name)', id(student_name))

print(student_name)


