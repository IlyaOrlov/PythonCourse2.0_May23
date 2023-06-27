import random

print('Укажите диапозон и попробуйте угадать число.\nЧтобы выйти напишите stop.')
d = int(input('Диапозон от 1 до: '))
number = random.randint(1, d)
while (a := input('Введите целое число : ')) != 'stop':
    if not a.isdecimal():
        print("Вы ввели НЕ число")
        continue
    a = int(a)
    if a == number:
        print('Поздравляю, вы угадали!')
        break
    elif a < number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
print('Пока')
