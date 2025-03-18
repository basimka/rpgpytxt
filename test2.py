Game = True
def menu_txt_fight():
    pass

class Evil:
    hp = 10
    damage = 10

class Player:
    hp = 100
    damage = 100
e = Evil()
p = Player()

def Proverka_death():
    if p.hp < 0:
        print("Вы проиграли")
        Game = False
        return Game
            
    elif e.hp < 0:
        print("Вы победили")
        Game = False
        return Game
    else:
        pass

def menu_fight():
    while Game == True:
        Game = True
        
        menu_txt_fight()
        n = input("Введите число: ")
        if n == '1':
            # Здоровье врага отнимает от вашего дамага.
            e.hp -= p.damage
            print('Вы ударили противника, у него осталось', e.hp)
            # Здоровье игрока отнимает от дамага врага.
            p.hp -= e.damage
            print('Противник ударил вас, у вас осталось',p.hp)

            print("*********************")
            Proverka_death()
        elif n == '2':
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0,5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            #print('Ваши хп',p.hp)

        
        
            

        print("******************")

menu_fight()