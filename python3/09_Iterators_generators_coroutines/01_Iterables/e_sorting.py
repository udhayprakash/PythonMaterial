#!/usr/bin/python3
"""
Purpose: sorted()
"""

student_tuples = [
    ("Ramesh", "A", 15),
    ("Ganesh", "C", 3),
    ("Suresh", "B", 12),
    ("Naresh", "B", 10),
]  #  0        1   2

print(student_tuples)
print()

# default - sorts by 0th element
print(sorted(student_tuples))
print(sorted(student_tuples, key=lambda x: x[0]))

print()
print(sorted(student_tuples, key=lambda x: x[2]))

print()  # There are two tuple with same 1st pos value
print(sorted(student_tuples, key=lambda x: x[1]))

print()
print(sorted(student_tuples, key=lambda x: (x[1], x[2])))


import operator

# print(dir(operator))
print(sorted(student_tuples, key=operator.itemgetter(1, 2)))

student_tuples.sort(key=operator.itemgetter(1, 2))
print(student_tuples)


# ----------------------------------------------------
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student("john", "A", 15),
    Student("jane", "B", 12),
    Student("dave", "B", 10),
]


sorted(student_objects, key=lambda student: student.age)  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

from operator import attrgetter, itemgetter

sorted(student_tuples, key=itemgetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter("age"))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# sorting by multiple values
sorted(student_tuples, key=itemgetter(1, 2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter("grade", "age"))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

# Ascending and Descending
sorted(student_tuples, key=itemgetter(2), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(student_objects, key=attrgetter("age"), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print()
student_tuples = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]
sorted(student_tuples, key=itemgetter(0))
# [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

sorted(student_tuples, key=itemgetter(1))
# [('blue', 1), ('red', 1), ('blue', 2), ('red', 2)]
