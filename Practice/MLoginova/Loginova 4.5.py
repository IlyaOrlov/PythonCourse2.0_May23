import random


def enter_chislo():
    while not (a := input("Введите число: ")).isnumeric():
        print("Вы ввели НЕ число")
    return int(a)


print("Привет! Давай ты задашь диапазон, я загадаю число из этого диапазона, а ты попробуешь его отгадать. Поехали!")
while (x := enter_chislo()) == (y := enter_chislo()):
    print("Нижняя и верхняя граница диапазона совпадают. Повторите ввод: ")
if x < y:
    n = random.randint(x, y)
    print("Загадано число в диапазоне от {} до {}, попробуй отгадать какое:".format(x, y))
else:
    n = random.randint(y, x)
    print("Загадано число в диапазоне от {} до {}, попробуй отгадать какое:".format(y, x))
while (p := enter_chislo()) != n:
    if p > n:
        print(f"Число {p} больше загаданного")
    else:
        print(f"Число {p} меньше загаданного")
print("Поздавляем! Вы угадали, это число - {} ".format(p))
