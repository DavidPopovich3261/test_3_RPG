from random import randint

class Weapon:
    @staticmethod
    def weapon():
        weapon_type=randint(0,2)
        type_w={'knife':0.5,'sword':1,'ax':1.5}
        for i ,j in enumerate(type_w.items()):
            if i==weapon_type:
                weapon=j
                return weapon
