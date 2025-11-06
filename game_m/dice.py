from random import randint

class Dice:
    @staticmethod
    def roll_dice(sides):
        dice=randint(1,sides)
        print(f"dice={dice}")
        return dice