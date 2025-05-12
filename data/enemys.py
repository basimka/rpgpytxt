class Enemy:
    def __init__(self,name,hp,damage,mana,haco,exp):
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.name = name
        self.haco = haco
        self.exp = exp
    def __str__(self):
        return str(self.name)
    
e = Enemy('мышь',80,10,0,20,10)
Rabbit = Enemy('кролик',100,15,0,20,20)
Mouse = Enemy('мышь',80,10,0,20,10)