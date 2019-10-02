class Employee:
    id = 0
    name = ""

    def __init__(self, i, n):
        print('constructor executed')
        self.id = i
        self.name = n

    def __call__(self, *args, **kwargs):
        print('printing args')
        print(*args)

        print('printing kwargs')
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


e = Employee(10, 'Pankaj')  # creating object

print(e)  # printing object

print(callable(e))

e()  # __call__
