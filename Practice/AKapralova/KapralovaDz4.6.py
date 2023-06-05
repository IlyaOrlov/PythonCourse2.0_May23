def maxmin(x, y):
    if x < y:
        print(y)
    else:
        print(x)


def maxmin2(x, y):
    if x < y:
        return y
    else:
        return x


x = int(input("Введите х: "))
y = int(input(f"Введите y: "))
maxmin(x, y)
print(f"Большее из вводимых чисел: {maxmin2(x, y)}")
