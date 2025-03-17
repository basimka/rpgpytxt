from random import randint
import menu_stats
import spisok_weapons

class Player:
    hp = 100
    damage = 10
    mana = 0
    thaco = 20

# Класс противника
class Enemy:
    name = 'Enemy'
    hp = randint(70,130)
    damage = randint(6,13)
    mana = 0
    thaco = 20

# #Класс оружия:
# class Weapon:
#     def __init__(self,damage,stability):
#         self.damage = damage
#         self.stability = stability
    

p = Player()
e = Enemy()


def versus():
    if versus == True:
        inta()
def inta():
    v = randint()
##########################
def game(p):
    while True:
        pass
##########################
menu_stats.menu_stats()
print (spisok_weapons.knife)
game(p)

