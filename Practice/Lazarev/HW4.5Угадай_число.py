import random

print('Укажите диапозон и попробуйте угадать число.\nЧтобы выйти напишите stop.')
d = int(input('Диапозон от 1 до: '))
number = random.randint(1, d)
a = int()
while (a := input('Введите целое число : ')) != 'stop':
    if not a.isdecimal():
        print("Вы ввели НЕ число")
    elif int(a) == number:
        print('Поздравляю, вы угадали!')
        break
    elif int(a) < number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
print('Пока')
