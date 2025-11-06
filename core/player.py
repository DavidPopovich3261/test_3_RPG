from core.character import Character
from random import randint

class Player(Character):
    def __init__(self,name):
        super().__init__(name,50)
        self.speed=randint(5,10)
        self.power=randint(5,10)
        self.armor_rating=randint(5,10)
        professioni=randint(0,1)
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







