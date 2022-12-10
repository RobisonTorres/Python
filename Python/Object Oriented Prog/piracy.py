print('Object Oriented Programming.')
print()

class Ship:
    """
    (...)
    Every time your spies see a new ship enter the dock, they will create a
    new ship object based on their observations.
    draft - an estimate of the ship's weight based on how low it is in the water
    crew - the count of crew on board.
    Taking into account that an average crew member on board adds 1.5 units
    to the draft, a ship that has a draft of more than 20 without crew is
    considered worthy to loot. Any ship weighing that much must have a lot of booty!
    """
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):

        # This function decides if a ship is worthy to loot.
        return self.draft - self.crew * 1.5 > 20

Titanic = Ship(36, 10)
print(Titanic.is_worth_it())  # Outputs - True.
print(Ship)
