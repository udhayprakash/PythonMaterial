#!/usr/bin/python3
"""
Purpose: 
    switch case is not implemented in python. 
    This script focuses on work-around for it.

pseudo-code:
    1. Addition 
    2. Subtraction
    3. Multiplication
    4. Division
    
"""
choice = int(input('Enter choice[1, 2, 3, 4]:'))
print('choice', choice, type(choice))

if choice == 1:
    print('Addition')
elif choice == 2:
    print('Subtraction')
elif choice == 3:
    print('Multiplication')
elif choice == 4:
    print('Division')
else:
    print('invalid choice')

# -------------------------------
result_for_choice = {
    1: 'Addition',
    2: 'Subtraction',
    3: 'Multiplication',
    4: 'Division',
}
# print(result_for_choice[choice])
print(result_for_choice.get(choice, 'invalid choice'))
