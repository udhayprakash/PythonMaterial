#!/usr/bin/python3
r"""
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


sum_of_values = (
    123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12 * 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
)
print(sum_of_values)


sum_of_values = (
    123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12 * 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
)
print(sum_of_values)


sum_of_values = [
    123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12 * 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
]
print(sum_of_values)


sum_of_values = {
    23
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12 * 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
    + 123
    + 23
    - 123 * 2 / 12
    - 123
    + 23
    - 123 * 2 / 12
}
print(sum_of_values)
