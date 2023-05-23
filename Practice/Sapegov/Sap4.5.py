import random


minimum = int(input('Введите нижнюю границу: '))
maximum = int(input('Введите верхнюю границу: '))
number = random.randint(minimum, maximum)
while True:
    i = input("Введите целое число: ")
    if isinstance(i, str):
        print('Вы ввели нечисловой символ!\nGame Over!')
        break
    elif int(i) < number:
        print('Не угадали! Загаданное число больше вашего.')
    elif int(i) > number:
        print('Не угадали! Загаданное число меньше вашего.')
    else:
        print('Поздравляю! Вы отгадали загаданное число!')
        break
