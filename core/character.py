class Character:
    def __init__(self,name,hp):
        self.hp=hp
        self.name=name

    def speak(self,character):
        print(f"{character.name}")

    def attack(self):
        pass


