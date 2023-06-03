def myf1(x, y):
    print(f"Вы ввели: {x } и {y }. Сравним.")
    if x > y:
        print(f"Наибольшее значение в паре {x}.")
    elif x == y:
        print(f"Введенные числа равны. {x} = {y}")
    else:
        print(f"Наибольшее значение в паре {y}.")


def myf2(x, y):
    if x > y:
        return x
    elif x == y:
        return x == y
    else:
        return y


a = int(input(f"Введите любое число: "))
b = int(input(f"Введите любое число: "))

myf1(a, b)

res = myf2(a, b)
print(f"Наибольшее  возвращаемое значение {res}")
