from random import randint
a = int(input('введите число'))
b = randint(1,10)
print('загаданое число', b)
if a == b:
    print('угадал')
else: print('не угадал')