# Список заклинаний

class Spells:
    def __init__(self,name,power,stability,mana):
        self.name = name
        self.damage = power
        self.mana = mana

    def __str__(self):
        return str(self.name)
    
fireball = Spells('Огненный шар',10,10)
lighting = Spells('молния',10,10)
heal = Spells('Лечение',10,10)
    
spisok = [fireball, lighting, heal]