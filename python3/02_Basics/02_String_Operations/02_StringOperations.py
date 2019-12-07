#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print('language       = ', language)
print('type(language) = ', type(language))

# my_string = 'what's next'  # SyntaxError: invalid syntax
my_string = 'what\'s next' 
print(my_string)

other_string = 'what\'s your next car\'s number '
print(other_string)

anoth_str = "as'asd'asd'asd'asd'sad'sad'sad'asd"
print(anoth_str)

anoth_str = 'AS"SAD"SDAS"SDASD"SDASD"SDASDDS"'
print(anoth_str)

anoth_str = '''what's your" next" car's no"'''
print(anoth_str)

"'"
'"'

''' " '" ' '''
""" ''' " '" ' ''' """

# multi-line strings
print('Today is an awesome day \
        to learn python')
print("Today is an awesome day \
        to learn python")

print()
print('''Today is an awesome day \
        to learn python''')
print("""Today is an awesome day \
        to learn python""")

print('''Today is an awesome day 
        to learn python''')
print("""Today is an awesome day 
        to learn python""")


print('''
a - apple
b - ball
c - cat
d - dog''')