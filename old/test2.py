# Для начала импортируем рандомайзер
from random import randint
print('Start Game')

############################## КЛАССЫ ##############################
class Player:
    def __init__(self,hp,damage,mana):
        self.hp = hp
        self.damage = damage
        self.mana = mana
    def __str__(self):
        pass

p = Player(100,10,0)
class Enemy:
    def __init__(self,hp,damage,mana):
        self.hp = hp
        self.damage = damage
        self.mana = mana
    def __str__(self):
        pass

e = Enemy(80,10,0)

class Room:
    def __init__(self, opisanie, exits):
        self.opisanie = opisanie
        self.exits = exits
        
        pass
    def __str__(self):
        pass
#Класс оружия:
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

spisok_weapon = [woodstick, clows, knife, sword, staff]

############################## Местность ###########################
def do_look():
    print(maplocation.opisanie)
############################## Инвентарь ###########################
def menu_inventory():
    print ('Ваши вещи = ' , inventar.things)
    print ('Ваши свитки = ' , inventar.scrolls)
    print ('Ваши бутылочки = ' , inventar.potions)
    print ('Свобдных слотов =' , inventar.limit)
    input("Нажмите Enter для продолжения.")

############################## Меню ################################
### Меню статистика
def menu_stats():
    print('Статистика игрок')
    print('****************')
    print (f'hp = {p.hp}')
    print (f'damage = {p.damage}')
    print (f'mana = {p.mana}')
    input("Нажмите Enter для продолжения.")

### Меню Битва
def menu_prefight():
    print (f'''
(1) Сражаться
(2) Посмотреть статистику           
(3) Вызвать меню помощи
(4) Выход из игры
''')
### Основное меню
def start_menu():
    print (f'''
Введите и нажмите  Enter
см (смотреть) - Осмотреться
хр (характеристики) - Характеристики
инв (инвентарь) - Инвентарь           
? (Помощь) - Вызвать меню помощи
выход (прочь) - Выход из игры
''')
### Меню помощи
def menu_help():
    print('####################################')
    print('Помочь ты сможешь только себе сам!!!')
    print('####################################')
############################## Игра ################################
def Game():
    start_menu()
    try:
        n=input('Введите число: ')
        if n == 'см' or 'смотреть':
            do_look()
        if n == 'смотреть':
            do_look()
        if n == 'хр':
            menu_stats()
        if n == 'характеристики':
            menu_stats()
        if n == 'инв':
            menu_inventory()
        if n == 'инвентарь':
            menu_inventory()
        if n == '?':
            menu_help()
        if n == 'помощь':
            menu_help()
        if n == 'выход':
            quit()
        if n == 'прочь':
            quit()
        else:
            pass
    except NameError:
        print('Введите число: ')
    except SyntaxError:
        print('Введите число: ')


############################## Комнаты ################################
class Room1:
    name = 'Комната'
    vihody = ['','','']
    orujie = sword
    opisanie =('###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n' + f'\
Валяется {sword}')
    

class Room2:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
Здесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room3:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room4:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room5:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room6:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room7:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')

class Room8:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')
    
class Room9:
    name = 'Комната'
    opisanie =('''
###################
Вы попали в {r1[0]}
###################
PЗдесь ни чего нет
###################
Выходы есть только:
на{}
''')
    
class inventar():
    things = []
    potions = []
    scrolls = []
    limit = 10


############################## Глобальные перемены #################
maplocation = Room1()
### Основной цикл
while True:
    Game()



