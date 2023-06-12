import random

print('Укажите диапозон и попробуйте угадать число')
d = int(input('Диапозон до: '))
number = random.randint(0, d)
while (a := int(input('Введите целое число : '))) != -1:
    # не нашел как сделать break при нечисловом символе
    # как сделать print('Пока') при вводе -1 ?
    if a == number:
        print('Поздравляю, вы угадали!')
        break
    elif a < number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
        continue
