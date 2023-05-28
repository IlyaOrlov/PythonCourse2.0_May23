def maxmin(x, y):
    if x > y:
        print(f"Максимальное число равно {x}")
        a = x
    else:
        print(f"Максимальное число равно {y}")
        a = y
    return a


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = maxmin(x, y)
