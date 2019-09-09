#!/usr/bin/python
"""
Purpose: Demonstration of String Operations
"""

language = 'Python Programming'
print('language       = ', language)
print('type(language) = ', type(language))

myString = 'what\'s next'
print(myString)

junkData = '$%^%^    &^* &^\'*&^ * uhk'  # escaping '
print('junkData       = ', junkData)
print('type(junkData) = ', type(junkData))

junkData = "$%^%'^&^* &^'*&^' * uhk"  # single quote enclosed in double quotes
print('junkData       = ', junkData)
print('type(junkData) = ', type(junkData))


print("'")
print('"')
print('\'')

print(" ''' ' '''  ")

print('""')
print("''")

print(''' """ """ ''')
print(""" ''' ''' """)


# multi-line string 
print('TOday is an awesome day\
            to work ')

print("TOday is an awesome day\
            to work ")

print()
print('''TOday is an awesome day\
            to work ''')
print("""TOday is an awesome day\
            to work """)


print('''TOday is an awesome day
            to work ''')
print("""TOday is an awesome day
            to work """)
