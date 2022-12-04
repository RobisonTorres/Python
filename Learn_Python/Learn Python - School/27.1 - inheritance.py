print('From Free Code Camp')
print()

class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

an1 = PartyAnimal('dog')
an1.party()

an1_points = FootballFan('cat')
an1_points.touchdown()
