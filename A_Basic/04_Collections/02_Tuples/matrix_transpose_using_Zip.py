matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

print 'ORIGINAL matrix:', matrix
for row in matrix:
    print row

# transposed_matrix = zip(matrix[0], matrix[1], matrix[2])   
transposed_matrix = zip(*matrix)

print 
print 'TRANSPOSED matrix:', transposed_matrix
for row in transposed_matrix:
    print row

"""
>>> zip([1], [3])
[(1, 3)]
>>> zip('aaa', 'bcd'
... )
[('a', 'b'), ('a', 'c'), ('a', 'd')]
>>>
>>>
>>>
>>> zip('aaa', 'bc'
... )
[('a', 'b'), ('a', 'c')]
>>>
>>> map(None, 'aaa', 'bcd')'
  File "<stdin>", line 1
    map(None, 'aaa', 'bcd')'
                           ^
SyntaxError: EOL while scanning string literal
>>> map(None, 'aaa', 'bcd')
[('a', 'b'), ('a', 'c'), ('a', 'd')]
>>> map(None, 'aa', 'bcd')
[('a', 'b'), ('a', 'c'), (None, 'd')]
>>> map(None, 'aaa', 'bc')
[('a', 'b'), ('a', 'c'), ('a', None)]
>>>
"""