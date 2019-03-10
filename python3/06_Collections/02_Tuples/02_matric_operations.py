from __future__ import print_function

matrix = [
    (1, 2, 3),
    [4, 5, 6],
    (7, 8, 9)
]

print('ORIGINAL matrix:', matrix)
for row in matrix:
    print(row)


print('\n==============')

first_row = []
second_row = []
third_row = []
for row in matrix:
    first_row.append(row[0])
    second_row.append(row[1])
    third_row.append(row[2])

print(first_row)
print(second_row)
print(third_row)

transposed_matrix = [
    first_row,
    second_row,
    third_row
    ]
print('transposed_matrix:{}'.format(transposed_matrix))

