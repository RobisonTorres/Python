import random
print('Object Oriented Programming.')
print()

class Ghost(object):
    """
    Create a class Ghost - Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of "white" or "yellow" or
    "purple" or "red" when instantiated
    """
    def __init__(self):

        # It gives a attribute of color to a ghost object.
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])

g1 = Ghost()
print(g1.color)  # Outputs - white or yellow or purple or red.
