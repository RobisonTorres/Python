print('Object Oriented Programming.')
print()

class Person:

    # Assigning different attributes to the class.
    def __init__(self, name, age, country='Brazil'):  # Brazil is a default value.
        self.name = name
        self.age = age
        self.country = country
        # print(self.name + '- object made.')  # It shows when a new object is created.

    # A function inside the class.
    def my_func(self):
        print('Hello, my name is ' + self.name + '.')
        print('I\'m ' + str(self.age) + ',')
        print('and I\'from ' + self.country + '.')

    # Classes can also have class attributes, created by assigning variables within
    # the body of the class.
    condition = 'Condition: Student.'

# To create new objects to the class Person.
p1 = Person('John', 36, 'Canada')  # p1 and p2 are objects.
p2 = Person('Jorge', 40)

# p1.age = 22  # Updating age.
# del p1.age  # deleting age p1.
# del p1  # deleting p1 object.

# Printing name and age.
print(p1.name, p1.age)
print(p2.name, p2.age)
print()

# Printing function and condition.
p1.my_func()
print(p1.condition)
print()
p2.my_func()
print(p1.condition)
print()
