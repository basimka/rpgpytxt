# Для начала импортируем рандомайзер
from random import randint

class door_lock:
    def __new__(cls,diff):
        open = randint(0,diff)
        return open

    

lockdr = door_lock(20)

def unlock():   
    lk = input(f'Введите значение от 0 до 10: ')
    if str(lk) != str(lockdr):
        print('Вам не удалось открыть \n')
        print(lockdr)

    elif str(lk) == str(lockdr):
        print('Вам удалось открыть замок!!! \n')
        print(lockdr)
while True:
    unlock()

