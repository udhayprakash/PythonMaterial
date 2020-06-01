#!/usr/bin/python
"""
Purpose: Importance and usage of multiple quotes
"""
language = 'Python Programming'
print(language, type(language))

my_string = 'How are you?'
print(my_string)

# my_string = 'What's up?'   # SyntaxError: invalid syntax
my_string = 'What\'s up?'   
print(my_string)
# NOTE 1: Placing \ before any operator with result in treating operator as a
# ordinary character

other_string = 'What\'s going in yours\' in-laws\' house'
print(other_string)

other_string = "What's going in yours' in-laws' house"
print(other_string)

some_other_str = '''What's up in yours' daugther's "wedding"'''
print(some_other_str)

some_other_str = """ python -c 'awdwad' asdss "sfdsdfd", '''dedfdfwef sd -m jd;jd''' """
print(some_other_str)

print('\n\n')
# '\''
# "'"
# '"'
# ''' '""' ''''
# """ ''' '""' '''' """

# Multi-line Strings 
print('Today is an awesome day \
          to learn python')
print("Today is an awesome day \
          to learn python")
print('''Today is an awesome day \
          to learn python''')
print("""Today is an awesome day \
          to learn python""")

print()
print('''Today is an awesome day 
          to learn python''')
print("""Today is an awesome day 
          to learn python""")


print('''
    a - apple
    b - ball
    c - cat
    d - dog''')

# NOTE 2: triple quote strings are multi-line strings
