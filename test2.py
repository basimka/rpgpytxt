# Для начала импортируем рандомайзер
from random import randint
print('Start Game')
############################## Глобальные перемены #################

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

############################## Местность ###########################
def do_look():
    print('''
Ни чего не видно. Хоть глаз выколи.
''')
############################## Инвентарь ###########################
def menu_inventory():
    pass

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
(1) Осмотреться
(2) Характеристики
(3) Инвентарь           
(4) Вызвать меню помощи
(5) Выход из игры
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
        if n == '1':
            do_look()
        if n == '2':
            menu_stats()
        if n == '3':
            menu_inventory()
        if n == '4':
            menu_help()
        if n == '5':
            quit()
        else:
            pass
    except NameError:
        print('Введите число: ')
    except SyntaxError:
        print('Введите число: ')
### Основной цикл
while True:
    Game()