from pprint import pp

from package4 import *  # wildcard import

# print(globals())
pp(globals)
print()

import package4 as p4

print(dir(p4))
print(dir(p4.module1))
