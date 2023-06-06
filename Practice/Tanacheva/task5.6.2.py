def myfun(x, y):
    rez = 0
    if x >= y:
        rez = x
    else:
        rez = y
    return rez


x1 = int(input("Введите число1:"))
y1 = int(input("Введите число2:"))
rez1 = myfun(x1, y1)
print(f"Большее введеное число {rez1}")
