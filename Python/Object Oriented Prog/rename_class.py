print('Object Oriented Programming.')
print()

class Class:
    pass
    '''
    (...) prepare some function, which could change name of a given class. 
    '''
def class_name_changer(cls, new_name):

    # There's no need to use the return statement.
    if new_name[0].isupper() and new_name.isalnum():  # Rules
        cls.__name__ = new_name
    else:
        raise Exception('error')  # It should raise an error if rules are not followed.

print(class_name_changer(Class, 'MyClass'), Class.__name__)  # Outputs - MyClass.
