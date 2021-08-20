#!/usr/bin/python3
"""
Purpose: Working with Named Tuples

Named Tuples can be:
    1. access by index - like normal tuples
    2. access by keyname - like dictionaries
    3. using getattr()
"""
import collections

student_details = ('Arjun', 26, '23/07/1992')
#                    0      1         2
print(f'{type(student_details)=}')
print(f'{student_details      =}')

# Accessing Values - using index
print('Student Name:', student_details[0])
print('Student Age :', student_details[1])
print('Student DOB :', student_details[2])

# Step 1: created Named Tuple object
Students = collections.namedtuple('Students', ['name', 'age', 'dob'])

# Step 2: create tuples using that object
student_details2 = Students('Santosh', 25, '04/04/1993')

# Accessing Values - using index 
print()
print('Student Name:', student_details2[0])
print('Student Age :', student_details2[1])
print('Student DOB :', student_details2[2])

# Accssing Values - using position names 
print()
print('Student Name:', student_details2.name)
print('Student Age :', student_details2.age)
print('Student DOB :', student_details2.dob)


print()
print(f"{getattr(student_details2, 'name') =}")
assert student_details2.name == getattr(student_details2, 'name')
assert student_details2.age == getattr(student_details2, 'age')
assert student_details2.dob == getattr(student_details2, 'dob')

# student_details2[4]       # IndexError: tuple index out of range
# student_details2.full_name  # AttributeError: 'Students' object has no attribute 'full_name'
# getattr(student_details2, 'full_name') # AttributeError: 'Students' object has no attribute 'full_name'

print(f"{hasattr(student_details2, 'full_name') =}")

if hasattr(student_details2, 'full_name'):
    getattr(student_details2, 'full_name')

if hasattr(student_details2, 'dob'):
    print(f"{getattr(student_details2, 'dob') =}")



# Named Tuples are also immutable 
# student_details2[1] = 45            # TypeError: 'Students' object does not support item assignment
# student_details2.age = 45           # AttributeError: can't set attribute
# setattr(student_details2, 'age', 45)  # AttributeError: can't set attribute