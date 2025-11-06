from core.monsters import Monsters
from core.Rond import Rond

class Orc(Monsters):
    def __init__(self,name):
        super().__init__(name,50)
        self.speed=Rond([0,5]).rond
        self.power=Rond([10,15]).rond
        self.armor_rating=Rond([2,8]).rond
        self.type='orc'



