from random import randint
from media.pictures import pic_Start
from data.player import *
from data.enemys import *
from data.weapons import *
#from data.menu_stats import *
#Объявление глобальной переменной агрессия
#Если агрессия есть то значит и по шапке получить можно
global agressive
agressive = 0

###Приветственный экран
pic_Start()
####################### Комнаты ##################################
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

# Инвентарь. Было принято решение вынести инвентарь в отдельный класс.
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
    print(maplocation.opisanie)
    if maplocation.orujie != 0:
        print (f'Валяется {maplocation.orujie}')
    if maplocation.vragy != 0:
        print (f'В углу скалится {maplocation.vragy}')

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
        if maplocation.orujie != 0:
            print ('\n Что вы хотите взять? \n')
            print (maplocation.orujie)
            vz = input('Введите название предмета: ')
            if str(vz) == str(maplocation.orujie):
                print (f'Вы взяли {maplocation.orujie}')
                inv.things.append(maplocation.orujie)
                inv.str_things.append(str(maplocation.orujie))
                maplocation.orujie = 0
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
                quit()
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
        
### Основноe меню
start_menu()

############################## Глобальные переменные ###########################
#global x
#x = 1
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