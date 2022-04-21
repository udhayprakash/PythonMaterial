#!/usr/bin/python
"""
Purpose: Importance of Class Variables
"""


# class definition
class Employee(object):
    """
    common base class for employees
    """

    emp_count = 0  # class variable

    def __init__(self, name, salary=20000):
        """
        This is a constructor method
        :param name:
        :param salary:
        """
        print("\n New Employee joined")
        self.employee_name = name
        self.salary = salary
        Employee.emp_count += 1

    def total_employees_count(self):
        """
        This method is used to display the count of employees
        :return:
        """
        print(f"Total Employees count: {Employee.emp_count}")

    def __del__(self):
        """
        This is destructor method - defaulty called,
        when the instance is deleted
        :return:
        """
        print("\nDestructor is called")
        Employee.emp_count -= 1


if __name__ == "__main__":
    # instantiation
    empl_1 = Employee("Udhay", 200000)
    print(vars(empl_1))
    empl_1.total_employees_count()

    empl_2 = Employee("Prakash")
    print(vars(empl_2))
    empl_2.total_employees_count()

    # deleting the empl_1
    del empl_1

    empl_3 = Employee("Akhila")
    print(vars(empl_3))
    empl_3.total_employees_count()


# =================================================
# class variables can be modified at instance level,
# by the changes will reflect only to that instance
class Demo:
    counter = 10

    def change_counter(self):
        self.counter += 1


obj1 = Demo()
print(Demo.counter, end=" ")
obj1.change_counter()
print(Demo.counter)

obj2 = Demo()
print(Demo.counter, end=" ")
obj2.change_counter()
print(Demo.counter)
