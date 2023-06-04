#!/usr/bin/python
"""
Purpose:
"""
import ast
from pprint import pprint


def main(python_script):
    with open(python_script, "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"import": [], "from": []}

    def visit_Import(self, node):
        for alias in node.names:
            self.stats["import"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.stats["from"].append(alias.name)
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)


if __name__ == "__main__":
    main(python_script="../../08_Decorators/18_functools_lru_cache.py")


# cp d_ast_ex.py d_ast_ex.py.bak && python -m autopep8 -i d_ast_ex.py
