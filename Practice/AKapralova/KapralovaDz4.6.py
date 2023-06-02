def maxmin(x, y):
    if int(x) < int(y):
        print(y)
    else:
        print(x)


x = int(input("Введите х: "))
y = int(input(f"Введите y: "))
maxmin(x, y)


def maxmin(x, y):
    if x < y:
        return y
    else:
        return x


x = int(input("Введите х: "))
y = int(input(f"Введите y: "))
print(f"Большее из вводимых числе: {maxmin(x, y)}")
