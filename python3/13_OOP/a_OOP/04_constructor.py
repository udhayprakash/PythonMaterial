"""
Purpose: constructor is a method which will be
    called the moment instance is created
"""
from pprint import pp


class Person(object):
    """class definition"""

    my_class_var = 111  # class - level variable

    def __init__(self):
        print("New instance is born! Adding default features")
        self.inst_var = 222
        local_var = 333
        # return 123  # TypeError: __init__() should return None, not 'int'
        # NOTE: Construction should return only None

    def instance_method(self):
        return "This is an instance method"


# Instantiation
p1 = Person()
print(p1)

print(Person.instance_method(p1))
print(p1.instance_method())
assert p1.instance_method() == Person.instance_method(p1)


# p1.__init__() # But NOT RECOMMEND, as code duplicate execution

for each_attribute in dir(p1):
    print(each_attribute)

print()

# To get only the instance variables
print(f"p1.__dict__: {p1.__dict__}")
print(f"vars(p1)   : {vars(p1)}")
assert vars(p1) == p1.__dict__
print()


print("vars(Person):")
pp(vars(Person))
print()
# -------------------------------------------------

pp(vars())  # pp(globals())

# Note: calling the vars() function without parameters will
# return a dictionary containing the local symbol table.


"""
Assignment:
    run below in shell
    vars(list)
    vars(str)
    vars(dict)
"""
