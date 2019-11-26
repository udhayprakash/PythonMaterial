#!/usr/bin/python
"""
Purpose: Importance of class Variables
"""


# class Definition
class Employee:
    """
    common base class for employee
    """
    empcount = 0  # class variable

    def __init__(self, name, salary):
        """
        This is a constructor method
        :param name:
        :param salary:
        """
        print('\nInstance is born')
        self.name = name  # instance variable
        my_var = 'something'  # ordinary variable
        self.salary = salary
        Employee.empcount += 1

    def display_count(self):
        """
        This method is used to display the count
        :return:
        """
        print("total employee%s" % Employee.empcount)

    def display_employee(self):
        """
        This method is used to display employee salary details
        :return:
        """
        print(("name:", self.name, ",salary:", self.salary))

    def __del__(self):
        """
        default destructor
        :return:
        """
        Employee.empcount -= 1
        print('Destructor is called')


# Instantiation

emp_1 = Employee('Fabina', 5000)
print(vars(emp_1))
print(f'Total no. of employees:{Employee.empcount}')

emp_2 = Employee('Rehman', 3500)
print(f'Total no. of employees:{Employee.empcount}')

emp_3 = Employee('Teju', 7800)
print(f'Total no. of employees:{Employee.empcount}')

del emp_1
print(f'Total no. of employees:{Employee.empcount}')


print()
print('last statement')


"""
Assignment
    Tesla company 
        class variable: chase number
            instance variables
                - car_model
                - car color
                - car price
            
            display()
        
"""