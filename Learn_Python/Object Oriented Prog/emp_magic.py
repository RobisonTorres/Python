print('Object Oriented Programming.')
print()

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):  # It can be used to recreate an object.
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):  # To get readable info about the object.
        return f'Employee{self.fullname()} - {self.email}'

    def __add__(self, other):  # To add values from different objects.
        return self.pay + other.pay

    def __len__(self):  # To get the length of full name.
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 1200)
emp_2 = Employee('Test', 'User', 1500)

print(repr(emp_1))
print(str(emp_1))
print(emp_1)
print(emp_1 + emp_2)
print(len(emp_1))
