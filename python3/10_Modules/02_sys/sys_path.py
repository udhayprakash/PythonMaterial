import sys

print(type(sys.path))

# append custom path 
# sys.path.insert(0, '/usr/bin/python')

for each in sys.path:
    print(each)
