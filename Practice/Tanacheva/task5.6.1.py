def myfun(x, y):
    rez = 0
    if x >= y:
        rez = x
    else:
        rez = y
    print(f"Большее веденное число: {rez}")


x1 = int(input("Введите число1:"))
y1 = int(input("Введите число2:"))
myfun(x1, y1)
