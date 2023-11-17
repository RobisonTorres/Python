print('Object Oriented Programming.')
print()

class Human():
    '''
    You have to do God's job. The creation method must return an array of length 2
    containing objects (representing Adam and Eve). The first object in the array 
    should be an instance of the class Man. The second should be an instance of the
    class Woman. Both objects have to be subclasses of Human. Your job is to implement
    the Human, Man and Woman classes.
    '''
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class Man(Human):

    def __init__(self, job):
        self.job = job

class Woman(Human):

    def __init__(self, job):
        self.job = job

def God():

    # This function creates humans.    
    person1 = Man('John')
    person2 = Woman('Jasmine')
    return [person1, person2]
