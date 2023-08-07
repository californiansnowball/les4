from random import randint
import time
while True:
    print('ты готов?')
    time.sleep(1)
    print(3, end = '')
    time.sleep(1)
    print(2, end = '')
    time.sleep(1)
    print(1, end = '')
    time.sleep(1)
    a = randint(1,3)
    if a == 1:
        print('камень')
    if a == 2:
        print('ножницы')
    if a == 3:
        print('бумага')
