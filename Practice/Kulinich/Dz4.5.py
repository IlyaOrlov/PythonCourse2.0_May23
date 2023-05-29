import random


x = input("Введите минимальное число диапазона от  ")
y = input("Введите максимальное число диапазона до  ")
v = random.randint(int(x),int(y))
while (z := input("Угадайте число  ")).isnumeric():
    if int(z) == v:
        input("Вы угадали  ")
    elif int(z) < v:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')


