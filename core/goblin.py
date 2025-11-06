from core.monsters import Monsters
from core.Rond import Rond


class Goblin(Monsters):
    def __init__(self, name):
        super().__init__(name, 20)
        self.speed = Rond([5, 10]).rond
        self.power = Rond([5, 10]).rond
        self.armor_rating =1
        self.type = 'goblin'

