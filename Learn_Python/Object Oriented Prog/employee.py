import datetime
print('Object Oriented Programming.')
print()

class Employee:

    raise_amount = 1.05
    n_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.n_employees += 1  # In this way,
        # I can keep track of the total number of employee.
        # This is very useful to accumulate data as the objects are created.

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # Using 'self' in raise amount it allows changes.

    @classmethod  # This is a decorator.
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        # This function changes the raise amount of the class.

    @classmethod  # Alternative constructor. It allows to create objects from strings.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # It doesn't have connection with the variables
    # or the attributes of the class.
    def is_workday(day):
        if day.weekday() in (5, 6):  # 5 and 6 equals to saturday and sunday resp.
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 1200)
emp_2 = Employee('Test', 'User', 1500)

print(emp_1)

my_date = datetime.date(2022, 6, 18)
print(emp_1.is_workday(my_date))

'''
Tutorial 1

print(emp_1.fullname())  # It needs parentheses because it is a method.
print(Employee.fullname(emp_1))  # It does the same as the upper line.
_______________________________________________________________________________________
Tutorial 2

print(Employee.__dict__) - Information about the class.

Class Variable - It is the same for each instance.
n_employees = 0

        Employee.n_employees += 1  # In this way,
        # I can keep track of the total number of employees.
        # This is very useful to accumulate data as the objects are created.

print(emp_1.pay)  # Outputs - 1200
emp_1.apply_raise()

Employee.raise_amount = 1.04  # I can change the raise amount for every employee.
emp_1.raise_amount = 1.10  # I can also change the raise amount for each one.
# It creates a variable within the instance.

print(emp_1.__dict__)
{'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 
'email': 'Corey.Schafer@company.com'}

With raise amount variable.
{'first': 'Corey', 'last': 'Schafer', 'pay': 1386, 'email': 
'Corey.Schafer@company.com', 'raise_amount': 1.1}

print(emp_1.pay)  # Outputs - 1260
print(emp_2.pay)  # Outputs - 1500

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)  # Outputs - 1386 - with .10
print(emp_2.pay)  # Outputs - 1560 - with .04
        
print(Employee.n_employees)  # 2
_______________________________________________________________________________________
Tutorial 3

Employee.raise_amount = 1.04  # I can change the raise amount for every employee.
Or using a class method:

    @classmethod  # This is a decorator.
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        # This function changes the raise amount of the class.
    
    @classmethod  # Alternative constructor. It allows to create objects from strings.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
emp_str_1 = 'John-Doe-70000'

emp_3 = Employee.from_string(emp_str_1)
print(emp_3.fullname())
print(emp_3.email)

    @staticmethod  # It doesn't have connection with the variables
    # or the attributes of the class.
    def is_workday(day):
        if day.weekday() in (5, 6):  # 5 and 6 equals to saturday and sunday resp.
            return False
        return True
my_date = datetime.date(2022, 6, 18)
print(emp_1.is_workday(my_date))
  
'''
