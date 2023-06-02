import random


def enter_chislo():
    while not (a := input("Введите число: ")).isdecimal():
        print("Вы ввели НЕ число")
    return int(a)

print("Привет! Давай ты задашь диапазон, я загадаю число из этого диапазона, а ты попробуешь его отгадать. Поехали!")
x = enter_chislo()
y = enter_chislo()
#проверка на совпадение нижней и верхней границы
while x == y:
    print("Нижняя и верхняя граница диапазона совпадают. Повторите ввод: ")
    x = enter_chislo()
    y = enter_chislo()
if x < y:
    n = random.randint(x, y)
    print("Загадано число в диапазоне от {} до {}, попробуй отгадать какое:".format(x, y))
else:
    n = random.randint(y, x)
    print("Загадано число в диапазоне от {} до {}, попробуй отгадать какое:".format(y, x))
while poisk := enter_chislo():
    if poisk > n:
        print("Число больше загаданного")
    elif poisk < n:
        print("Число меньше загаданного")
    elif poisk == n:
         print("Поздавляем! Вы угадали, это число - {} ".format(poisk))
         break
