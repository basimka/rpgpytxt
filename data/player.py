# Это класс Персонажа, так как версия игры сейчас однопользовательская
# то экземпляр класса Игрока только один
class Player:
    inventar = []
    inventar_str = []
    def __init__(self, hp, damage, mana, haco):
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.haco = haco
    lvl = 1   
    exp = 0
    if exp >= 256000:
        lvl = 10
    elif exp >= 128000:
        lvl = 9
    elif exp >= 64000:
        lvl = 8
    elif exp >= 32000:
        lvl = 7
    elif exp >= 16000:
        lvl = 6
    elif exp >= 8000:
        lvl = 5
    elif exp >= 4000:
        lvl = 4
    elif exp >= 2000:
        lvl = 3
    elif exp >= 1000:
        lvl = 2
    def __str__(self):
        pass

global p

p = Player(100,10,0,20)