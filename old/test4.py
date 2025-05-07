from random import randint

class Lock:
    def __init__(self,diff):
        self.diff = randint(0, diff)

    def unlock(self):
        vzlom = input ("ВВедите число от 0 до 10 ")
        if int(vzlom) == int(self.diff):
            print ("Вы открыли замок!!!")
        else:
            print ("ЗАКРЫТО!!!")
            print (self.diff)

    def __str__(self):
        pass

class Chest:
    def __init__(self):
        pass

    def __str__(self):
        pass
    
zamok = Lock(10)

while True:
    zamok.unlock()

