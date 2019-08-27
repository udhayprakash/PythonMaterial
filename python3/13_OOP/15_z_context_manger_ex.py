# context mangers

class ManagedFile:
    def __init__(self, name, mode= 'r'):
        self.name = name
        self.file_operation_mode =  mode

    def __enter__(self):
        self.file = open(self.name, self.file_operation_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# with open('hello.txt', 'w') as f:
#     f.write('I am good')
#     f.close()

with ManagedFile('hello.txt', 'w') as f:
    f.write('I am good')
    f.close()

#################################################
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __enter__(self):
        print("in __enter__")
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        print("in __exit__")
    def divide_by_zero(self):
        # causes ZeroDivisionError exception
        return self.width / 0

with Rectangle(3, 4) as r:
    # exception successfully pass to __exit__
    r.divide_by_zero()

# Output:
# "in __enter__"
# "in __exit__"
# Traceback (most recent call last):
#   File "e0235.py", line 27, in <module>
#     r.divide_by_zero()