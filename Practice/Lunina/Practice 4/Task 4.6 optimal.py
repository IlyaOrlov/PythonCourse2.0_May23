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


while not (a := input(f"Введите 1 число: ")).isdecimal() \
        or not (b := input(f"Введите 2 число: ")).isdecimal():
    print("Вы ввели не число.")
else:
    print("Отлично! Приступим к сравнению.")
    a = int(a)
    b = int(b)
    myf1(a, b)


res = myf2(a, b)
print(f"Наибольшее  возвращаемое значение {res}")
