from core.monsters import Monsters
from random import randint


class Goblin(Monsters):
    def __init__(self, name):
        super().__init__(name, 20)
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating =1
        self.type = 'goblin'

