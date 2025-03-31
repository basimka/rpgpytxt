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

class Room1:
    name = 'Комната'
    vihody = ['ю','з','']
    orujie = sword
    vragy = []
    opisanie =('###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n' + f'\
Валяется {sword}')
    
#print (len(Room1.vihody))

for room in Room1.vihody:
    print (room)