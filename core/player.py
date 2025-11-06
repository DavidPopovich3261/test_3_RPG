from core.character import Character
from core.Rond import Rond

class Player(Character):
    def __init__(self,name):
        super().__init__(name,50)
        self.speed=Rond([5,10]).rond
        self.power=Rond([5,10]).rond
        self.armor_rating=Rond([5,15]).rond
        professioni=Rond([0,1]).rond
        if professioni:
            self.profession='fighter'
            self.power+=2
        else:
            self.profession='cure'
            self.hp+=10

    def speak(self):
        print(f"{self.name,self.profession}")

    def attack(self):
        pass







