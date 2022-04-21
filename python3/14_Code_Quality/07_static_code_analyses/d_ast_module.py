#!/usr/bin/python
"""
Purpose: AST(Abstract Syntax Tree) Module
    Usage
        - Making IDEs intelligent and making a feature everyone knows as intellisense.
        - Tools like Pylint uses ASTs to perform static code analysis
        - Custom Python interpreters

    - Modes of Code Compilation
        - exec: We can execute normal Python code using this mode.
        - eval: To evaluate Python’s expressions, this mode will
                return the result fo the expression after evaluation.
        - single: This mode works just like Python shell which
                execute one statement at a time.
"""

import ast

# Executing code
code = ast.parse("print('Hello world!')")
print(f"{code       =}")
print(f"{type(code) =}")

exec(compile(code, filename="", mode="exec"))

# To see AST created for above object
print(f"{ast.dump(code) =}")
print("\n\n")


# Evaluating Python Expression
expression = "6 + 8"
code = ast.parse(expression, mode="eval")
print(f"{code       =}")
print(f"{type(code) =}")

print(eval(compile(code, "", mode="eval")))

# To see AST created for above object
print(f"{ast.dump(code) =}")
print("\n\n")


# Constructing multi-line ASTs
tree = ast.parse(
    """
fruits = ['grapes', 'mango']
name = 'peter'

for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
"""
)

print(ast.dump(tree))
print("\n\n")


class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str("String: " + tree_node.s)


class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        print("{}".format(tree_node.s))


tree_node = ast.parse(
    """
fruits = ['grapes', 'mango']
name = 'peter'

for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
"""
)

NodeTransformer().visit(tree_node)
NodeVisitor().visit(tree_node)
