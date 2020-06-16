#!/usr/bin/python
"""
Purpose: Inner function example
    Scoping - LEGB
"""
pi = 300
mydict = {'lang': 'python'}

# function definition
def outer(given):
    print('outer function - start ')
    pi = 200
    mydict = {'lang': 'ruby'}

    # inner()    # UnboundLocalError: local variable 'inner' referenced before assignment
    def inner():
        print('inner function - start')
        pi = 100
        mydict = {'lang': 'golang'}
        print(f'pi              :{pi}')
        print(f'mydict["lang"]  :{mydict["lang"]}')
    
    if given % 2 == 0:  # even:
        inner()

if __name__ == '__main__':
    outer(123)
    # inner()  # NameError: name 'inner' is not defined
    print()
    outer(124)