print('введите оценки')
three = int(input('введите количество троек'))
four = int(input('четверок'))
five = int(input('пятерок'))
sum = three*3 + four*4 + five*5
count = five + four + three
res = sum/count
print('твой средний балл', res)
if res == 5:
    print('ты отличник')
if res < 5 and res >= 4:
    print('ты хорошист')
if res < 4:
    print('ты троечник')
