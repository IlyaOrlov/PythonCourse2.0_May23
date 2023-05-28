import random


a = input("Введите нижнюю границу диапазона: ")
while not a.isdecimal():
    print("Вы ввели НЕ число")
    a = input("Введите нижнюю границу диапазона: ")
b = input("Введите верхнюю границу диапазона: ")
while not b.isdecimal():
    print("Вы ввели НЕ число")
    b = input("Введите верхнюю границу диапазона: ")
n = random.randint(int(a), int(b))
print("Загадано число от {} до {}, попробуйте отгадать какое?".format(a, b))
poisk = input("Введите предпологаемое число: ")
while poisk.isdecimal() and int(poisk) != n:
    if not poisk.isdecimal():
        print("Вы ввели нечисловой символ")
    if int(poisk) != n:
        if int(poisk) > n:
            print("Вы ввели число больше загаданного")
        else:
            print("Вы ввели число меньше загаданного")
    poisk = input("Введите предпологаемое число: ")
    if int(poisk) == n:
        print("Поздавляем! Вы угадали, это число - {} ".format(poisk))
