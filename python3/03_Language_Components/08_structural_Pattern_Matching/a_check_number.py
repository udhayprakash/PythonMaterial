#!/usr/bin/python3
"""
Purpose: Structural Pattern Matching
    - new in python 3.10
    - Syntax:
        match <expression>:
            case <pattern 1> [<if guard>]:
                <handle pattern 1>
            case <pattern n> [<if guard>]:
                <handle pattern n>
    - It is much more than the traditional "switch cases", available in other languages
"""

num1 = 123

# Method 1 - using traditional if-else conditions
if num1 >= 0:
    print(f"{num1} is positive")
else:
    print(f"{num1} is negative")


# Method 2 - Using Structural pattern Matching
# match num1:
#     case num1 >= 0:
#         print(f"{num1} is positive")
#     case _:
#         print(f"{num1} is negative")


match num1 >= 0:
    case True:
        print(f"{num1} is positive")
    case False:
        print(f"{num1} is negative")


# -----------------------------------------------------
num2 = int(input("Enter some integer:"))

if num2 % 2 == 0:
    print(f"{num2} is EVEN number")
else:
    print(f"{num2} is ODD number")


match num2 % 2 == 0:
    case True:
        print(f"{num2} is EVEN number")
    case False:
        print(f"{num2} is ODD number")
