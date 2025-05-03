from random import randint

class Lock:
    def __init__(self,diff):
        self.diff = diff
    
    @staticmethod
    def difficult():
        d1 = randint(0, 10)
        return d1
    
    dd = difficult()

    def unlock(self,d1):
        vzlom = input ("ВВедите число от 0 до 10 ")
        if int(vzlom) == int(d1):
            print ("Вы открыли замок!!!")
        else:
            print ("ЗАКРЫТО!!!")
            print (d1)

    def __str__(self):
        pass
    
zamok = Lock(10)

while True:
    zamok.unlock(zamok.dd)