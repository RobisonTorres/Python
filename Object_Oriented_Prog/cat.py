print('Object Oriented Programming.')
print()

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' makes a noise.'

class Cat(Animal):
    '''
    Your task is to complete the Cat class which Extends Animal and replace
    the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
    '''
    def speak(self):  

        # This function changes the Parent Class method 'speak'.
        return self.name + ' meows.'
