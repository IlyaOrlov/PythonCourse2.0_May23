def maxmin(x, y):
    if x > y:
        print(f"Максимальное число равно {x}")
    else:
        print(f"Максимальное число равно {y}")


def maxmin2(x, y):
    if x > y:
        return x
    else:
        return y


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
maxmin(a,b)
z = maxmin2(a, b)
print(z)
