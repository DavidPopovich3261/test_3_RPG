

class Character:
    def __init__(self,name,hp):
        self.hp=hp
        self.name=name

    def speak(self,type):
        print(f"{self.name,type}")

    def attack(self):
        pass
