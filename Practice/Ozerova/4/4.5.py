import random


x = int(input("Введите минимальное значение диапазона: "))
y = int(input("Введите максимальное значение диапазона: "))
z = random.randint(x, y)
while True:
    n = input("Угадайте, загаданное число из диапазона: ")
    if not n.isdigit():
        print("Вы ввели не число, введите число: ")
    a = int(n)
    if a < x:
        print("Нет, загаданное число больше, введите другое: ")
    elif a > x:
        print("Нет, загаданное число меньше, введите другое: ")
    else:
        print("Вы угадали!Ура!")
        break
