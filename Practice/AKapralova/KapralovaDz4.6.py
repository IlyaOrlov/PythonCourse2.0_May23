def maxmin(x, y):
    if int(x) < int(y):
        print(y)

    else:
        print(x)


x = int(input("Введите х: "))
y = int(input(f"Введите y: "))
maxmin(x, y)


def maxmin(x, y):
    if int(x) < int(y):
        return int(y)

    else:
        return int(x)


x = int(input("Введите х: "))
y = int(input(f"Введите y: "))
print(f"Большее из вводимых числе: {maxmin(x, y)}")
