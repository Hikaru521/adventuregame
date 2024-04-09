import random

class zombie:
    def __init__(self, nev, hp, dmg):
        self.nev = nev
        self.hp = hp
        self.dmg = dmg

mobs = {"Kémikus":zombie("Kémikus", 2000, random.randrange(20, 35)),
        "soldier":zombie("soldier", 50, random.randrange(25, 30)),
        "medve":zombie("medve", 100, random.randrange(30, 33)),
        "kutya":zombie("kutya", 75, random.randrange(20, 34))}

#print(mobs["kemikus_boss"].hp)





