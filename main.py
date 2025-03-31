# Для начала импортируем рандомайзер
from random import randint

############################## Оружие ###########################

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
##################################################################
class Room:
    name = 'Комната'
    vihody = ['ю','з']
    orujie = sword
    vragy = []
    opisanie =('\n\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n' + f'\
Валяется {sword}' + '\n\n')
    
class Room1:
    name = 'Комната1'
    vihody = ['в']
    orujie = sword
    vragy = []
    opisanie =('\n\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n' + f'\
Валяется {sword}' + '\n\n')

class Room2:
    name = 'Комната2'
    vihody = ['в','ю','']
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

class Room3:
    name = 'Комната3'
    vihody = ['ю','з']
    orujie = sword
    vragy = []
    opisanie =('\n\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n' + f'\
Валяется {sword}' + '\n\n')

class Room4:
    name = 'Комната4'
    vihody = ['в','ю','с','з']
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
    
class Room5:
    name = 'Комната5'
    vihody = ['в','ю']
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
    
class Room6:
    name = 'Комната6'
    vihody = ['с','з']
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
    
class Room7:
    name = 'Комната7'
    vihody = ['в','з','с']
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
    
class Room8:
    name = 'Комната8'
    vihody = ['в','с']
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

### Основная игровая функция
def deystvie(n):  
    global x
    global maplocation
    if n == 'см':
        do_look()
    elif n == 'смотреть':
        do_look()
    elif n == 'хр':
        menu_stats()
    elif n == 'характеристики':
        menu_stats()
    elif n == 'инв':
        menu_inventory()
    elif n == 'инвентарь':
        menu_inventory()
    elif n == '?':
        menu_help()
    elif n == 'помощь':
        menu_help()
    elif n == 'выход':
        quit()
    elif n == 'прочь':
        quit()
    elif n == 'ю':
        if maplocation.name == 'Комната':
            print('Вы перешли на юг')
            maplocation = Room3()
        elif maplocation.name == 'Комната1':
            print('Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('Тут стена, идти не куда')
    elif n == 'з':
        if maplocation.name == 'Комната':
            print('Вы перешли на запад')
            maplocation = Room1()
        elif maplocation.name == 'Комната1':
            print('Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('Тут стена, идти не куда')
    elif n == 'в':
        if maplocation.name == 'Комната':
            print('Тут стена, идти не куда')
        elif maplocation.name == 'Комната1':
            print('Вы перешли на восток')
            maplocation = Room()
        elif maplocation.name == 'Комната3':
            print('Тут стена, идти не куда')
            
    elif n == 'с':
        if maplocation.name == 'Комната':
            print('Тут стена, идти не куда')
        elif maplocation.name == 'Комната1':
            print('Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('Вы перешли на юсевер')
            maplocation = Room()
             
    else:
        print ('Ни чего не произошло')
        
### Основной цикл
start_menu()

############################## Глобальные переменные ###########################
global x
x = 1
global maplocation
maplocation = Room()

while True:
    n=input('Введите что нибудь: ')
    deystvie(n)
