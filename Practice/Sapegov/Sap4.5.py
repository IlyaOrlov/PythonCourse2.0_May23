import random


minimum = int(input('Введите нижнюю границу: '))
maximum = int(input('Введите верхнюю границу: '))
number = random.randint(minimum, maximum)
while True:
    i = input("Введите целое число: ")
    if not i.isdigit():
        print('Вы ввели нечисловой символ!\nGame Over!')
        break
    j = int(i)
    if j < number:
        print('Не угадали! Загаданное число больше вашего.')
    elif j > number:
        print('Не угадали! Загаданное число меньше вашего.')
    else:
        print('Поздравляю! Вы отгадали загаданное число!')
        break
