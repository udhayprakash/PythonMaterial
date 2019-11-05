#!/usr/bin/python

all_colors = {'red', 'blue', 'orange', 'yellow'}

colors_present = {'orange', 'blue'}

print(colors_present.issubset(all_colors))      # True
print(all_colors.issuperset(colors_present))    # True

print(all_colors.isdisjoint(colors_present))    # False

books = {'ramayana', 'bible'}
print(all_colors.isdisjoint(books))             # True

print(all_colors.isdisjoint(colors_present))
print(all_colors.intersection(colors_present))  # a INTERSECTION b
#
print(all_colors.union(colors_present))
print('all_colors.symmetric_difference(colors_present)')  # (A u B) - (A intersection B)
print(all_colors.symmetric_difference(colors_present))

print(all_colors - colors_present)  # {'red', 'yellow'}
print(colors_present - all_colors)  # set()
