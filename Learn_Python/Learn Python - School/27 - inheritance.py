print('3W School.')
print()

class Person:

    def __init__(self, name, age, country='Brazil'):
        # In this way, I can assign different values to my class.
        self.name = name
        self.age = age
        self.country = country

    def my_func(self):
        print('Hello, my name is ' + self.name + '.')
        print('I\'m ' + str(self.age) + ',')
        print('and I\'from ' + self.country + '.')

p1 = Person('John', 36, 'Norway')
print(p1.my_func())

class Student(Person):
    def __init__(self, name, age, majoring):
        super().__init__(name, age, country='Brazil')
        self.majoring = majoring

    def welcome(self):
        return f'{self.name}, your class of {self.majoring} is going to begin.'

s1 = Student('Rob', 27, 'Data Science')
print(s1.welcome())
