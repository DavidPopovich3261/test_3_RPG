from core.character import Character
from weapon import Weapon

class Monsters(Character):
    def __init__(self,name,hp):
        super().__init__(name,hp)
        self.weapon=Weapon.weapon()

    def speak(self):
        print(f"{self.name,self.type}")

    def attack(self):
        pass