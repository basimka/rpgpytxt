from random import randint

class Lock:
    def __init__(self,difficulty):
        self.diff = randint(1, difficulty)
        self.state = "Lock"

    def unlock(self):
        vzlom = input (f"Введите число от 0 до {self.diff} ")
        if int(vzlom) == int(self.diff):
            print ("Вы открыли замок!!!")
            self.state = "Unlock"
        print (self.state)

    def __str__(self):
        print (self.state)

class Chest:
    gold = 10
    zamok = Lock(10)

while True:
   Chest.zamok.unlock()
