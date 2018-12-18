
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



print Employee, type(Employee)
print vars(Employee)
# "this would create first object of employee class"

print
Emp1 = Employee("Udhay", 2000)  # "this would create second object of employee class"
print vars(Emp1)

print 'After Emp1 creation, Total employee count:', Employee.empcount

Emp2 = Employee("Prakash", 60000)
print 'Emp2.salary', Emp2.salary
print 'After Emp2 creation, Total employee count:', Employee.empcount


# Emp2 was terminated
del Emp2
print 'Total employee count:', Employee.empcount
