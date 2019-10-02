"""
Purpose:
sorted()
"""
sorted([5, 2, 3, 1, 4])  # [1, 2, 3, 4, 5]

a = [5, 2, 3, 1, 4]
a.sort()
a  # [1, 2, 3, 4, 5]

sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})  # [1, 2, 3, 4, 5]

list_of_strings = "This is a test string from Andrew".split()
sorted(list_of_strings)
# ['Andrew', 'This', 'a', 'from', 'is', 'string', 'test']
sorted(list_of_strings, key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])  # sort by age


# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# sorting by multiple values
sorted(student_tuples, key=itemgetter(1, 2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter('grade', 'age'))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]


# Ascending and Descending
sorted(student_tuples, key=itemgetter(2), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(student_objects, key=attrgetter('age'), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0))
# [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
