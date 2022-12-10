print('Object Oriented Programming.')
print()

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @ property  # In order to access a method like an attribute.
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @ property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter  # In this way, I can change the name.
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # In this way, I can delete an object.
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
# print(emp_1.email()) 'str' object is not callable '()'.
print(emp_1.email)
print()
emp_1.fullname = 'Rob Torres'
print(emp_1.email)

del emp_1.fullname
print(emp_1.__dict__)
