# Для начала импортируем рандомайзер
from random import randint
print('Start Game')

# Создадим класс игрока 
class Player:
    hp = 100
    damage = 10
    mana = 0
    exp = 0
    lvl = 0
    

# Класс противника
class Enemy:
    name = 'Enemy'
    hp = randint(70,130)
    damage = randint(6,14)
    mana = 0


### Меню статистика
def menu_stats():
    print('Статистика игрок')
    print('****************')
    print (f'hp = {p.hp}')
    print (f'damage = {p.damage}')
    print (f'mana = {p.mana}')
    input("Нажмите Enter для продолжения.")

# Список заклинаний

class Spells:
    def __init__(self,name,power,mana):
        self.name = name
        self.damage = power
        self.mana = mana

    def __str__(self):
        return str(self.name)
    
fireball = Spells('Огненный шар',10,10)
lighting = Spells('молния',10,10)
heal = Spells('Лечение',10,10)
    
spisok_magic = [fireball, lighting, heal]

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

#Инциализация классов
p = Player()
e = Enemy()

spisok_lvl_player = ['1000','2000','4000','8000','16000','32000','64000','128000','256000','512000']
#Для более простого использования обозвали классы Игрока и Противника #буквами p и e.
#Теперь нам надо запилить основное меню которое и будет запускаться при #старте
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
                menu_stats()
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
# Да, пытаться написать код в редакторе Дзен который будет еще и работать #после копи-паста это тот ещё геморрой!!!
### Меню Битвы
def menu_fight(p):
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

        if n == '2':
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0,5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            #print('Ваши хп',p.hp)

        else:
             print("Чего ждем?")
        if p.hp < 0:
            print("Вы проиграли")
        if e.hp < 0:
            print("Вы победили")

        print("******************")
# Меню помощи
def menu_help(p):
    print('####################################')
    print('Помочь ты сможешь только себе сам!!!')
    print('####################################')

def enemyEnable():
    pass
#Ну и собственно запускаем игру
###Запустить игру
menu(p)

#10.03.2025 - Пока работает выход из игры и просмотр статистики.
#10.03.2025 - Теперь можно драться и хилится