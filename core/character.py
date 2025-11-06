from game_m.dice import Dice

class Character:
    def __init__(self,name,hp):
        self.hp=hp
        self.name=name

    def speak(self,type):
        print(f"{self.name,type}")

    def attack(self,attacked):
        speed_attack=self.speed+ Dice.roll_dice(20)
        if speed_attack > attacked.armor_rating:
            return True
        return False

    def injury(self,injury):
        damage = self.power+Dice.roll_dice(6)
        if self.type != "plyer":
            damage*=self.weapon.values
        injury.hp-=damage




