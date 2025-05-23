# # Для начала импортируем рандомайзер
# from random import randint

# class chest:
#     pass

# class door_lock:
#     def __new__(cls,diff):
#         open = randint(0,diff)
#         return open

# lockdr = door_lock(10)

# def unlock():   
#     lk = input(f'Введите значение от 0 до 10: ')
#     if str(lk) != str(lockdr):
#         print('Вам не удалось открыть \n')
#         print(lockdr)

#     elif str(lk) == str(lockdr):
#         print('Вам удалось открыть замок!!! \n')
#         print(lockdr)

# while True:
#     unlock()

# Для начала импортируем рандомайзер
from random import randint

# Добавляем библиотеку с картинками
from media.pictures import pic_Start

#Объявление глобальной переменной агрессия
#Если агрессия есть то значит и по шапке получить можно
global agressive
agressive = 0

###Приветственный экран
pic_Start()
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

#Так как экземпляр класса Игрока у нас должен быть доступен отовсюду,
# то для начала мы делаем его глобальным, а потом уже создаем сам
# экземпляр класса
global p

p = Player(100,10,0,20)

#Экземпляр класса противника, во многом схож с игроком, но экземпляров класса будет куча
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
rabbit = Enemy('кролик',100,15,0,20,20)
mouse = Enemy('мышь',80,10,0,20,10)

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

####################### ЗамкИ ####################################



####################### Комнаты ##################################

class Room:  
    def __init__(self, name, exits, items, enemies):
        self.name = name
        self.exits = exits
        self.items = items
        self.enemies = enemies
    
    def get_items(self):
        res = "<пусто>"
        if self.items:
            res = " ".join(str(item) for item in self.items)
        return res

    def get_enemies(self):
        res = "<пусто>"
        if self.items:
            res = " ".join(str(enemie) for enemie in self.enemies)
        return res
        
    def __str__(self):
        return ('\n' + \
'######################################\n\t' 
+f'Вы попали в {self.name}\n'
+'######################################\n'
+'Выходы есть только:\n\t'
+f'{self.exits}\n'
+'В комнате лежит:\n\t'
+f'{self.get_items()}\n'
+'В комнате находятся:\n\t'
+f'{self.get_enemies()}\n')
    
    
r0 = Room('Комната', ['ю','з'], [sword], [mouse])
    
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


r1 = Room1()
r2 = Room2()
r3 = Room3()
r4 = Room4()
r5 = Room5()
r6 = Room6()
r7 = Room7()

# Инвентарь. Было принято решение вынести инвентарь в отдельный класс.
# Если всё пойдёт как надо то инвентарь из класса Player можно будет удалить
class inventar():
    golds = 0
    things = []
    str_things = []
    potions = []
    scrolls = []
    limit = 10

inv = inventar()    

######################### Меню Посмотреть###########################
def do_look():
    print(maplocation)
    # if maplocation.orujie != 0:
    #     print (f'Валяется {maplocation.orujie}')
    # if maplocation.vragy != 0:
    #     print (f'В углу скалится {maplocation.vragy}')

######################### меню Инвентарь ###########################
def menu_inventory():
    print ('Ваше золото = ' , inv.golds)
    print ('Ваши вещи = ' , inv.str_things)
    print ('Ваши свитки = ' , inv.scrolls)
    print ('Ваши бутылочки = ' , inv.potions)
    print ('Свобдных слотов =' , inv.limit)
    input("Нажмите Enter для продолжения.")

########################## Меню статистика #########################
def menu_stats():
    print('Статистика игрок')
    print('****************')
    print (f'hp = {p.hp}')
    print (f'damage = {p.damage}')
    print (f'mana = {p.mana}')
    print (f'exp = {p.exp}')
    print (f'На вас надеты = {p.inventar_str}')
    input("Нажмите Enter для продолжения.")

########################## Меню Битва #########################
### Пока не задействовано
def menu_prefight():
    print (f'''
(1) Сражаться
(2) Посмотреть статистику           
(3) Вызвать меню помощи
(4) Выход из игры
''')
    
########################## Основное меню #########################
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
    
############################ Меню Помощи #########################
def menu_help():
    print('####################################')
    print('Помочь ты сможешь только себе сам!!!')
    print('####################################')

############## Основная функция действия #########################
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
        print (inv.str_things)
        fg = input('Введите название предмета: ')
        i = 0
        while i < len(inv.things):
            if str(fg) == str(inv.things[i]):
                print (f'Вы надели {inv.things[i]}')
                p.inventar.append(inv.things[i]) 
                p.inventar_str.append(str(inv.things[i]))
                p.damage = p.damage + inv.things[i].damage
                del inv.things[i]
                del inv.str_things[i]
            i+=1

    elif n == 'напасть':
        if maplocation.vragy != 0:
            print ('На кого вы хотите напасть? \n')
            print (maplocation.vragy)
            fg = input('Введите название врага: ')
            if str(fg) == str(maplocation.vragy):
                print (f'Вы напали на {maplocation.vragy}')
                global agressive
                agressive = agressive + 1               
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
        if maplocation.items != 0:
            print ('\n Что вы хотите взять? \n')
            print (str(maplocation.get_items))
            vz = input('Введите название предмета: ')
            if str(vz) == str(maplocation.items):
                print (f'Вы взяли {maplocation.items}')
                inv.things.append(maplocation.items)
                inv.str_things.append(str(maplocation.items))
                maplocation.items = 0
    else:
        print ('Ни чего не произошло')

def proverka_enimy():
    pass

def fight():
    global agressive
    while agressive != 0:
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
                agressive = agressive - 1
            elif e.hp < 0:
                print("Вы победили")
                agressive = agressive - 1
                p.exp = p.exp + maplocation.vragy.exp
                maplocation.vragy = 0

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
        print(agressive)
### Основной цикл
start_menu()

############################## Глобальные переменные ###########################
global x
x = 1
global maplocation
maplocation = r0

global agressiv
agressiv = False

############################## Основной игровой цикл  ###########################
while True:
    # Предлагаем выбрать действие
    n = input('Введите что нибудь: ')
    # Обрабатываем выбранное действие
    deystvie(n)
    # Проверяем не напал ли на нас кто-то
    # Пока не работает
    proverka_enimy()