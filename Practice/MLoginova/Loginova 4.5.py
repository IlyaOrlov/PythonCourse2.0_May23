import random


def enter_chislo():
    while not (a := input("Введите число: ")).isnumeric():
        print("Вы ввели НЕ число")
    return int(a)


print("Привет! Давай ты задашь диапазон, я загадаю число из этого диапазона, а ты попробуешь его отгадать. Поехали!")
while (x := enter_chislo()) == (y := enter_chislo()):
    print("Нижняя и верхняя граница диапазона совпадают. Повторите ввод: ")
if x > y:
    x, y = y, x
n = random.randint(x, y)
print(f"Загадано число в диапазоне от {x} до {y}, попробуй отгадать какое: ")
while (p := enter_chislo()) != n:
    if p > n:
        print(f"Число {p} больше загаданного")
    else:
        print(f"Число {p} меньше загаданного")
print(f"Поздавляем! Вы угадали, это число - {p} ")
