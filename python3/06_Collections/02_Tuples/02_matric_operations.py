matrix = [
    (1, 2, 3),
    [4, 5, 6],
    (7, 8, 9)
]

print('ORIGINAL matrix:', matrix)
for row in matrix:
    print(row)

print('\n==============')

first_column = []
second_column = []
third_column = []
for row in matrix:
    first_column.append(row[0])
    second_column.append(row[1])
    third_column.append(row[2])

print('first_column ', first_column)
print('second_column', second_column)
print('third_column ', third_column)

transposed_matrix = [
    first_column,
    second_column,
    third_column
]
print('transposed_matrix:{}'.format(transposed_matrix))
