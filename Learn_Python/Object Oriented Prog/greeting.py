print('Object Oriented Programming.')
print()

class Person:
    """
    (...)
    Refactor the following code so that it belongs to a Person class/object.
    Each Person instance will have a greet method. The Person instance should
    be instantiated with a name so that it no longer has to be passed into each
    greet method call.
    """
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):

        # This function returns a greeting message for each person.
        return f'Hello {your_name}, my name is {self.name}.'

john = Person('John')
print(john.greet('Kate'))  # Outputs - Hello Kate, my name is John.
print(john.greet('Rob'))  # Outputs - Hello Rob, my name is John.
