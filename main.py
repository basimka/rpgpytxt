# Для начала импортируем рандомайзер
from random import randint


# Это класс Персонажа, так как версия игры сейчас однопользовательская
# то экземпляр класса Игрока только один
class Player:
    inventar = []
    def __init__(self,hp,damage,mana,haco):
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.haco = haco
    def __str__(self):
        pass

#Так как экземпляр класса Игрока у нас должен быть доступен отовсюду,
# то для начала мы делаем его глобальным, а потом уже создаем сам
# экземпляр класса
global p

p = Player(100,10,0,20)
class Enemy:
    def __init__(self,name,hp,damage,mana,haco):
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.name = name
        self.haco = haco
    def __str__(self):
        return str(self.name)

e = Enemy('мышь',80,10,0,20)



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
    vragy = e
    opisanie =('\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Выходы есть только:\n'+ f'\
{vihody}\n')
    
class Room1:
    name = 'Комната1'
    vihody = ['в']
    orujie = knife
    vragy = 0
    opisanie =('\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n')

class Room2:
    name = 'Комната2'
    vihody = ['в','ю','']
    orujie = sword
    vragy = 0
    opisanie =('###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Здесь ни чего нет\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n')

class Room3:
    name = 'Комната3'
    vihody = ['с',]
    orujie = staff
    vragy = 0
    opisanie =('\n' + '\
###################\n' + f'\
Вы попали в {name}\n'+'\
###################\n'+'\
Выходы есть только:\n'+f'\
{vihody}\n')

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
{vihody}\n')
    
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
{vihody}\n')
    
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
{vihody}\n')
    
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
{vihody}\n')
    
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
{vihody}\n')

r0 = Room()
r1 = Room1()
r2 = Room2()
r3 = Room3()
r4 = Room4()
r5 = Room5()
r6 = Room6()
r7 = Room7()

class inventar():
    golds = 0
    things = []
    potions = []
    scrolls = []
    limit = 10

inv = inventar()    


def do_look():
    print(maplocation.opisanie)
    if maplocation.orujie != 0:
        print (f'Валяется {maplocation.orujie}')
    if maplocation.vragy != 0:
        print (f'В углу скалится {maplocation.vragy}')
############################## Инвентарь ###########################
def menu_inventory():
    print ('Ваше золото = ' , inventar.golds)
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
взять - Поднять или взять что есть в комнате
надеть - Надеть что-то из инвентаря
напасть - Напасть на кого нибудь
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
        start_menu()
    elif n == 'помощь':
        start_menu()
    elif n == 'выход':
        quit()
    elif n == 'прочь':
        quit()
    elif n == 'надеть':
        print ('Что вы хотите надеть?')
        print (inv)
    elif n == 'напасть':
        if maplocation.vragy != 0:
            print ('На кого вы хотите напасть? \n')
            print (maplocation.vragy)
            fg = input('Введите название врага: ')
            if str(fg) == str(maplocation.vragy):
                print (f'Вы напали на {maplocation.vragy}')
                #maplocation.orujie = 0
                fight()
    elif n == 'ю':
        if maplocation.name == 'Комната':
            print('\n Вы перешли на юг')
            maplocation = r3
        elif maplocation.name == 'Комната1':
            print('\n Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('\n Тут стена, идти не куда')
    elif n == 'з':
        if maplocation.name == 'Комната':
            print('\n Вы перешли на запад')
            maplocation = r1
        elif maplocation.name == 'Комната1':
            print('\n Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('\n Тут стена, идти не куда')
    elif n == 'в':
        if maplocation.name == 'Комната':
            print('\n Тут стена, идти не куда')
        elif maplocation.name == 'Комната1':
            print('\n Вы перешли на восток')
            maplocation = r0
        elif maplocation.name == 'Комната3':
            print('\n Тут стена, идти не куда')
            
    elif n == 'с':
        if maplocation.name == 'Комната':
            print('\n Тут стена, идти не куда')
        elif maplocation.name == 'Комната1':
            print('\n Тут стена, идти не куда')
        elif maplocation.name == 'Комната3':
            print('\n Вы перешли на север')
            maplocation = r0
    elif n == 'взять':
        if maplocation.orujie != 0:
            print ('\n Что вы хотите взять? \n')
            print (maplocation.orujie)
            vz = input('Введите название предмета: ')
            if str(vz) == str(maplocation.orujie):
                print (f'Вы взяли {maplocation.orujie}')
                inventar.things.append(str(maplocation.orujie))
                maplocation.orujie = 0
                
    else:
        print ('Ни чего не произошло')


def proverka_enimy():
    pass

def fight():
    while e.hp > 0:
        # Также, как я и сказал по последовательности списка расставляет переменные.
        print('Вы hp:',p.hp)
        print('Вы damage: ',p.damage)
        print("**********************")
        print('Враг hp:',e.hp)
        print('Враг damage: ',e.damage)
        print("**********************")
        print("**********************")
        print("1)Ударить")
        print("2)Хил 0-5")
        n = input("Введите число: ")
        if n == '1':
            # Здоровье врага отнимает от вашего дамага.
            e.hp -= p.damage
            print('Вы ударили противника, у него осталось', e.hp)
            # Здоровье игрока отнимает от дамага врага.
            p.hp -= e.damage
            print('Противник ударил вас, у вас осталось',p.hp)
            print("*********************")
            if p.hp < 0:
                print("Вы проиграли")
            elif e.hp < 0:
                print("Вы победили")


        elif n == '2':
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0,5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            #print('Ваши хп',p.hp)
        else:
             print("Чего ждем?")
        print("******************")
### Основной цикл
start_menu()

############################## Глобальные переменные ###########################
global x
x = 1
global maplocation
maplocation = r0

while True:
    n = input('Введите что нибудь: ')
    deystvie(n)
    #do_look()
    proverka_enimy()
