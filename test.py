class Weapon:
    def __init__(self,name,damage,stability):
        self.name = name
        self.damage = damage
        self.stability = stability

    def __str__(self):
        return str(self.name)

woodstick = Weapon('Палка',10,5)
clows = Weapon('Когти',20,20)
knife = Weapon('Нож',20,10)
sword = Weapon('Меч',25,15)
staff = Weapon('Посох',15,15)

class inventar():
    golds = 0
    things = [sword,staff,sword]
    str_things = []
    potions = []
    scrolls = []
    limit = 10

inv = inventar()

i =0

while i < len(inv.things):
    inv.str_things.append(str(inv.things[i]))
    i+=1

print (inv.things[0])
print (sword)
print (inv.str_things)