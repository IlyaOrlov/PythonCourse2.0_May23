def minmax():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x > y:
        print("Большее число:", x)
    else:
        print("Большее число:", y)

def maxmin():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    if x > y:
        return x
    else:
        return y

# Вызов функции minmax
minmax()

# Вызов функции maxmin
result = maxmin()
print("Большее число:", result)