print('From Code Wars')
print()

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})"\
        .format(self.name, self.health, self.damage_per_attack)
    __repr__ = __str__

def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name \
        else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name

print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
