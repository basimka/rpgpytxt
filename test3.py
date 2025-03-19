# def Proverka(x,y):
#     if (x == '10'):
#         y = 1
#         return x,y
#     elif(x == '1'):
#         print ('x = 1')

# def Fight():
#     Game = True
#     while Game == True:
#         x = input('Введите икс')
#         y = 55
#         Proverka(x,y)
#         print (Proverka(x,y))

# Fight()

tipeRoom = ['болото','лес','комната']
exitsRoom = ['n','s','w','e']
class Room:
    def __init__(self, name, opisanie, exits):
        self.name = name
        self.opisanie = opisanie
        self.exits = exits
        
    def __str__(self):
        return str(self.name)

r = Room(1,1,1)
print(r)


class Room1:
    def __init__(self, name, exits):
        self.name = name
        self.exits = exits 
        self.name = tipeRoom[name]
    exits = ['','',]
    def __str__(self):
        return str(self.name)

r1 = Room1(1,1)
print(r1)