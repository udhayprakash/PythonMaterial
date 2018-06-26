
class Employee:
    "common base class for employee"
    empcount = 0  # class variable

    def __init__(self, name, salary):
        self.name = name   # instance variable
        self.salary = salary
        Employee.empcount += 1

    def displaycount(self):
        print "total employee%s" % Employee.empcount 

    def displayemployee(self):
        print("name:", self.name, ",salary:", self.salary)

    def __del__(self):
        """
        destructor
        :return:
        """
        Employee.empcount -= 1
        print 'Destructor is called'


# "this would create first object of employee class"


Emp1 = Employee("Udhay", 2000)  # "this would create second object of employee class"
print 'Total employee count:', Employee.empcount

Emp2 = Employee("Prakash", 60000)
print 'Total employee count:', Employee.empcount


# Emp2 was terminated
del Emp2
print 'Total employee count:', Employee.empcount
