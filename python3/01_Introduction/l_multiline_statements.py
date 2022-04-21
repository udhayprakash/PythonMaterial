#!/usr/bin/python3
"""
Purpose: Working with Multi-line statements

    Python is a interpreter-based language
        - Each line executes separates
        - \ -> Line Continuation Operator
        - WIll join more than one line to a single statement

Brace
    ()  paranthesis

    []  square braces
    {}  flower braces

PEP 8 :
    a) Lines should be 79 characters in length or less
    b) Continuations of long expressions onto additional lines should be
       indented by four extra spaces from their normal indentation level.

"""
sum_of_values = 123 + 23 - 123 * 2 / 12
print(sum_of_values)

sum_of_values = 12 + 45 + 34534545 + 343 - 34234 + 34 + 454 + 42534 + 34 / 34\
                   + 45 + 34534545 + 343 - 34234 + 34 + 454 + 42534 + 34 / 34\
                   + 45 + 34534545 + 343 - 34234 + 34 + 454 + 42534 + 34 / 34\
                   + 45 + 34534545 + 343 - 34234 + 34 + 454  # arithmetic operation
print(sum_of_values)   # display the result
# NOTE:After line continuation operator, even comments should not be added

sum_of_values = (12 + 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234 + 67
                 + 454 - 435 - 43534 - 34 + 454 +
                 42534 + 34 / 34 + 34534 -
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234)
print(sum_of_values)


sum_of_values = [12 + 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234 + 67
                 + 454 - 435 - 43534 - 34 + 454 +
                 42534 + 34 / 34 + 34534 -
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234]
print(sum_of_values)


sum_of_values = {12 + 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234 + 67
                 + 454 - 435 - 43534 - 34 + 454 +
                 42534 + 34 / 34 + 34534 -
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 45 + 34534545 + 343 - 34234 + 34 +
                 454 + 42534 + 34 / 34 + 34534 + 34234}
print(sum_of_values)
