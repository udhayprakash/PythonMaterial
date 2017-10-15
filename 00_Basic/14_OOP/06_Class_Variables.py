class Employee:
    "comman base class for employee"
    empcount = 0  # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displaycount(self):
        print("total employee%" % Employee.empcount)

    def displayemployee(self):
        print("name:", self.name, ",salary:", self.salary)


# "this would create first obkect of employee class"


Emp1 = Employee("zara", 2000)  # "this would create second obkect of employee class"
Emp2 = Employee("manni", 60000)
