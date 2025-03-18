def Proverka(x,y):
    if (x == '10'):
        y = 1
        return x,y
    elif(x == '1'):
        print ('x = 1')

def Fight():
    Game = True
    while Game == True:
        x = input('Введите икс')
        y = 55
        Proverka(x,y)
        print (Proverka(x,y))

Fight()

