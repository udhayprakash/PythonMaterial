#!/usr/bin/python

# eval expects only strings, bytes or code object
print(eval('5'))
print(eval('5 * 34 - 2342/2 %23 //3'))

print(eval(b'5'))
print(eval(b'5 * 34 - 2342/2 %23 //3'))

eval('print("hello world")')

print('-' * 20)
# exec expects print within the string code to display
print(exec('5'))
exec("print('Hello world!')")

print('\n############### AST ##################')
import ast

code = ast.parse('5 * 34 - 2342/2 %23 //3', mode='eval')
print(type(code), code)
print(eval(compile(code, '', mode='eval')))

code = ast.parse("print('Hello world!')")
print(type(code), code)
exec(compile(code, filename='', mode='exec'))
print(ast.dump(code))

# Multi-line ast
print()
tree = ast.parse('''
fruits = ['grapes', 'mango']
name = 'peter'

for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
''')

print(ast.dump(tree))
exec(compile(tree, filename='', mode='exec'))

# NOTE: Tools like Pylint uses ASTs to perform static code analysis
