# Список заклинаний

class Spells():
    def __init__(self,name,damage,stability,mana):
        self.name = name
        self.damage = damage
        self.stability = stability
        self.mana = mana

    def __str__(self):
        return str(self.name)