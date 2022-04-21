import collections

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# inserts 4 at the end of deque
de.append(4)

print('The deque after appending at right is :\n', de)

# inserts 6 at the beginning of deque
de.appendleft(6)

print('\nThe deque after appending at left is :\n', de)

# deletes 4 from the right end of deque
print(de.pop())

print('\nThe deque after deleting from right is :\n', de)

# deletes 6 from the left end of deque
print(de.popleft())

# printing modified deque
print('\nThe deque after deleting from left is:\n', de)

# using count() to count the occurrences of 3
print('\nThe count of 3 in deque is:', de.count(3))

# using remove() to remove the first occurrence of 3
print(de.remove(3))

print('\nThe deque after deleting first occurrence of 3:')
print(de)

# adds 4,5,6 to right end
de.extend([4, 5, 6])
print('\nThe deque after extending deque at end is:\n', de)

# adds 7,8,9 to right end
de.extendleft([7, 8, 9])
print('\nThe deque after extending deque at beginning:\n', de)

# rotates by 3 to left
de.rotate(-3)
print('\nThe deque after rotating deque is:')
print(de)

# using reverse() to reverse the deque
de.reverse()

print('\nThe deque after reversing deque is:')
print(de)

# NOTE: below works in python 3 only
# using index() to print the first occurrence of 4
print('The number 4 first occurs at a position : ')
print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)
