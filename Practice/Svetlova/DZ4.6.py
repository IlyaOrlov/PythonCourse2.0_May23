def maxmin(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))


# Вызов функции maxmin
result = maxmin(x, y)
print("Большее число:", result)

