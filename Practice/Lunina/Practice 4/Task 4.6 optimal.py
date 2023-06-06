def myf1(x, y):
    print(f"Вы ввели: {x} и {y}")
    if x > y:
        print(f"Наибольшее значение в паре {x}.")
    elif x == y:
        print(f"Введенные числа равны. {x} = {y}")
    else:
        print(f"Наибольшее значение в паре {y}.")


def myf2(x, y):
    if x >= y:
        return x
    else:
        return y


def check_num(n):
    while not (x := input(f"Введите {n} число: ")).isdecimal():
        print("Вы ввели не число.")
    return x


a = int(check_num(1))
b = int(check_num(2))
print("Отлично! Приступим к сравнению.")
myf1(a, b)

res = myf2(a, b)
print(f"Наибольшее  возвращаемое значение {res}")
