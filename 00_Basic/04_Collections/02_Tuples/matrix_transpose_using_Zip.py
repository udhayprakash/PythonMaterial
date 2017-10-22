matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

print 'ORIGINAL matrix:'
for row in matrix:
    print row 

transposed_matrix = zip(*matrix)

print 'TRANSPOSED matrix:'
for row in transposed_matrix:
    print row 