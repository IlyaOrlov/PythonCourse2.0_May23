import random
x = int(input("Задайте числовой диапазон игры\nВведи левую границу диапазона: "))
y = int(input("Введи правую границу диапазона: "))
chislo = random.randint (x, y)
while True:
    if  z := input("Угадай число, которое я загадал: "):
        if not z.isdigit():
            print("Вы ввели не числовой символ\nИгра окончена")
            break
    w = int(z)
    if w == chislo:
        print("Поздравляю! Число угадано.")
        break
    elif w > chislo:
        print("Попробуем ещё разок. Твоё число больше загаданного: ")
    else:
        print("Попробуем ещё разок. Твоё число меньше загаданного: ")
