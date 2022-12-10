print('Object Oriented Programming.')
print()

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)  # Let the Employee class handles this.
        self.pro_lang = pro_lang

emp_1 = Employee('Corey', 'Schafer', 1200)
emp_2 = Employee('Test', 'User', 1500)

dev_1 = Developer('Rob', 'Torres', 3000, 'Python')
dev_2 = Developer('John', 'Doe', 1000, 'Java')


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees  # List of employees the manager supervises.

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

man_1 = Manager('Sue', 'Smith', 90000, [dev_1])

man_1.add_emp(dev_2)
man_1.remove_emp(dev_1)
man_1.print_emp()

print(isinstance(man_1, Developer))  # Outputs - False
print(issubclass(Developer, Employee))  # Outputs - True
