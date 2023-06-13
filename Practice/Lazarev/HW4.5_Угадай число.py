import random

print('Укажите диапозон и попробуйте угадать число')
d = int(input('Диапозон от 1 до: '))
number = random.randint(1, d)
while (a := input('Введите целое число : ')) != 'stop':
##    a = int(a) 
    if not a.isdecimal():
        print("Вы ввели НЕ число")
        #break если оставить, то код завершится,
        #а вдруг юзер случайно, нужно дать щанс исправиться)
    elif int(a) == number:
        print('Поздравляю, вы угадали!')
        break
    elif int(a) < number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
print('Пока')

