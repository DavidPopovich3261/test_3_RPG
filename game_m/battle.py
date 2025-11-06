from game_m.dice import Dice

class Battle:
    def __init__(self,player, monster):
        self.player=player
        self.monster=monster

    def first_turn(self):
        value_player=Dice.roll_dice(6)+self.player.speed
        value_monster=Dice.roll_dice(6)+self.monster.speed
        if value_monster > value_player:
            return 'monster1'
        return 'player1'

    def attack(self,first_turn1):
        if first_turn1 =='monster1':
            attack=self.monster.attack(self.player)
            if attack:
                self.monster.injury(self.player)
        else:
            attack=self.player.attack(self.monster)
            if attack:
                self.player.injury(self.monster)



