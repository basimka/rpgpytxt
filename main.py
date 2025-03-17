from random import randint
print('Start Game')

class Player:
    hp = 100
    damage = 10
    mana = 0

p = Player()

class Enemy:
    hp = randint(70,130)
    damage = randint(6,13)
    mana = 0

e = Enemy()

#Основной цикл игры
def menu(p):
    while True:
        print('(1) Сражаться')
        print('(2) Посмотреть статистику')
        print('(3) Вызвать меню помощи')
        print('(4) Выход из игры')
        try:
            n=input('Введите число: ')
            if n == '1':
                menu_fight(p)
            if n == '2':
                menu_stats(p)
            if n == '3':
                menu_help(p)
            if n == '4':
                quit()
            else:
                print('Выбери себе')

        except NameError:
            print('Введите число')
        except SyntaxError:
            print('Введите число')

### Меню Битвы
def menu_fight(p):
    pass

### Меню статистика
def menu_stats(p):
    print('Статистика игрок')
    print('****************')
    print ('hp = ', p.hp)
    print ('damage = ',p.damage)
    input("Нажмите Enter для продолжения.")

# Меню помощи
def menu_help():
    pass


###Запустить игру
menu(p)
