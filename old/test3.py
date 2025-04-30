from random import randint

class Lock:
    def __init__(self,diff):
        self.diff = diff

    @staticmethod
    def difficult():
        d1 = randint(0,10)
        return d1

    def unlock(self):
        vzlom = input ("ВВедите число от 0 до 10 ")
        if vzlom == self.difficult():
            print ("Вы открыли замок!!!")
        else:
            print ("ЗАКРЫТО!!!")
            print (self.difficult())

    def __str__(self):
        pass
    

zamok = Lock(10)

while True:
    zamok.unlock()