#!/usr/bin/python3
"""
Purpose: Generator Expressions
    and chained generator Expressions
"""
listCompr = [i for i in range(7)]
print(f"{listCompr} {type(listCompr)}")

setCompr = {i for i in range(7)}
print(f"{setCompr} {type(setCompr)}")

dictCompr = {i: i**2 for i in range(7)}
print(f"{dictCompr} {type(dictCompr)}")


genExpr = (i for i in range(7))
print(f"{genExpr} {type(genExpr)}")  # generator

# -----
integers = list(range(8))
squared = (i * i for i in integers)
negated = (-i for i in squared)

print(type(negated), negated)
for each in negated:
    print(each)

# ----

squared = (i * i for i in integers)
negated = (-i for i in squared)

print(list(negated))
