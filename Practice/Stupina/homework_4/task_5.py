import random


while not (d := input('Введите желаемый диапазон через ",": ')).replace(',', '').isdecimal() or d.find(',') == -1:
    print('Диапазон введён некорректно')
d = d.split(',')
x = random.randint(int(d[0]), int(d[1]))

while (y := input('Загаданное число = ')).isdecimal():
    int_y = int(y)
    if int_y == x:
        print('Вы угадали!')
        break
    elif int_y < x:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
