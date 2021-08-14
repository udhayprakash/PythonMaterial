# class Demo:
#     counter =10
#     def change_counter(self):
#         self.counter += 1

# obj1 = Demo()
# print(Demo.counter, end= ' ')
# obj1.change_counter()
# print(Demo.counter)

# class Parent:
#     def __init__(self, var1):
#         self.__var1 = var1

#     def get_var1(self):
#         return self.__var1

# class Child(Parent):
#     def __init__(self, var1, var2):
#         super().__init__(var1)
#         self.var2 = var2


# obj1 = Child(10, 20)

# print(obj1.get_var1(), obj1.var2)


# class Player:
#     def play(self):
#         return 'playing'

# class Cricketer(Player):
#     def play(self):
#         return super().play()

# print(Cricketer().play() == Player().play())


# class Address:
#     def __init__(self, city):
#         self.__city = city

#     def get_city(self):
#         return self.__city

# class Student:
#     def __init__(self, id, marks, address):
#         self.__address = address
#         self.id = id
#         self.marks = marks

#     def get_address(self):
#         return self.__address

# s1 = Student(1, 90, Address('Mysore'))
# print(s1.get_address().get_city())


# class Student:
#     def __init__(self, id, marks):
#         self.id = id
#         self.__marks = marks

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

#     def __add__(self, other):
#         print(other.get_marks() - self.get_marks())


# Student(1, 90) + Student(2, 40)

import os
from pprint import pprint
from collections import Counter

os.chdir('..')
print(f'{os.getcwd() =}')

extensions = Counter()
for cur_dir, dirs, files in os.walk(os.getcwd()):
    if '.git' in cur_dir:
        continue
    for file in files:
        filename, file_extn = os.path.splitext(file)
        if file_extn != '.py':
            extensions.update((file_extn,))
        if file_extn in ('.mp4'): 
            complete_file = os.path.join(os.getcwd(),cur_dir, file)
            print(complete_file)
            # os.remove(complete_file)
            # os.rename(complete_file, os.path.join(os.getcwd(),cur_dir, filename+'.png'))
        # if file_extn in ('.p', '.1', '.2', '.3', '.4'):

pprint(extensions)

import matplotlib.pyplot as plt
# Plot
plt.pie(extensions.values(), labels=extensions.keys(), 
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
