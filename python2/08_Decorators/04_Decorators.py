#!/usr/bin/python
"""
Purpose:  decorators example
"""
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print('<\______/>')
    return wrapper

def ingredients(func):
    def wrapper():
        print('#tomatoes#')
        func()
        print('~salad~')
    return wrapper

def sandwich(food='--ham--'):
    print(food)

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>


print('-'*80)
print('============Using decorators===')

@bread
@ingredients
def sandwich(food='--ham--'):
    print(food)

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

#
# print('-'*80)
# print('============order of declaration of decorators matters===')
#
# @ingredients
# @bread
# def strange_sandwich(food="--ham--"):
#     print(food)
#
# strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
