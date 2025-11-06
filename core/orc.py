from core.monsters import Monsters
from random import randint

class Orc(Monsters):
    def __init__(self,name):
        super().__init__(name,50)
        self.speed=randint(0,5)
        self.power=randint(10,15)
        self.armor_rating=randint(2,8)
        self.type='orc'



