#!/usr/bin/python
"""
Purpose: To display the astrickes in a half-diamond pattern
"""
i=0
while i <10:
    i+=1
    print('*' * i)

# print(f'i={i}')
# i = 10
while i > 0:
    i -=1
    print('*' * i)

###########
j=0
while j <10:
    j +=1
    print( ' '*(10-j) + '*' * j )

# print(f'j={j}')
while j > 0:
    j -= 1
    print( ' '*(10-j) + '*' * j )


#############  FULL DIAMOND
p = 0
while p < 10:
    print( ' '*(10-p) + '*' * 2 * p )
    p += 1

while p > 0:
    print( ' '*(10-p) + '*' * 2 * p )
    p -= 1

#############  FULL DIAMOND

for p in range(10):
    print( ' '*(10-p) + '*' * 2 * p )

for p in range(10,0, -1):
    print( ' '*(10-p) + '*' * 2 * p )

#############  FULL DIAMOND

for p in range(10):
    if p %2:
        print(('*' * p).center(10) )
for p in range(10, 0, -1):
    if p %2:
        print(('*' * p).center(10) )