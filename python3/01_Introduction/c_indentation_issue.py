#!/usr/bin/python


print("hello world")   
print('hello world')       # IndentationError: unexpected indent



# block code - if, elif , for,  while, class,  functions


summation = 34 + 99                                    
# dynamic typed languages 

print(summation)     

print("Summation result is ", summation)  # , (comma) operator works as a logic separator

# for i in range(9):
# print(i)            # IndentationError: expected an indented block

for i in range(9):
    print(i)

if 2 < 3:
   print('2 < 3')

if 2 < 3:
    if 2 < 6:
        if 2 < 62:
            print('2 < 3 < 6')
    print()


# tabs vs white-space
# PEP 8 (Python Enhancement Proposal) - code style guide
# four white-spaces