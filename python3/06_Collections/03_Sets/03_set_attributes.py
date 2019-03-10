
all_colors = {'red', 'blue', 'orange', 'yellow'}

colors_present = {'orange', 'blue'}


print(colors_present.issubset(all_colors))
print(all_colors.issuperset(colors_present))


books = {'ramayana', 'bible'}

print(all_colors.isdisjoint(books))


print(all_colors.isdisjoint(colors_present))
print(all_colors.intersection(colors_present))  # a INTERSECTION b

print('all_colors.symmetric_difference(colors_present)') # (A u B) - (A intersection B)
print(all_colors.symmetric_difference(colors_present))

print(all_colors - colors_present)
print(colors_present - all_colors)
