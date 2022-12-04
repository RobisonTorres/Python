print('3W School.')
print()

class Person:
    student = 'student'  # Classes can also have class attributes,\
    # created by assigning variables within the body of the class.

    def __init__(self, name, age, country='Brazil'):
        # In this way, I can assign different values to my class.
        self.name = name
        self.age = age
        self.country = country

    def my_func(self):
        print('Hello, my name is ' + self.name + '.')
        print('I\'m ' + str(self.age) + ',')
        print('and I\'from ' + self.country + '.')

p1 = Person('John', 36, 'Canada')  # p1 and p2 are objects.
p2 = Person('Jorge', 40)

# p1.age = 22  # Updating age.
# del p1.age
# del p1
# print(p1.name, p1.age)  # Equals to John 36
# print(p1)  # Equals to <__main__.Person object at 0x0000024603085FD0>

p1.my_func()
p2.my_func()
print(p1.name, p1.student)
