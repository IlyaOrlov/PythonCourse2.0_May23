def outer_decor(fun):
    def inner_decor(*args, **kwargs):
        print("======")
        result = fun(*args, **kwargs)
        print("======")
        return result

    return inner_decor


@outer_decor
def myf1(x, y):
    print(f"Вы ввели: {x} и {y}")
    if x > y:
        print(f"Наибольшее значение в паре {x}.")
    elif x == y:
        print(f"Введенные числа равны. {x} = {y}")
    else:
        print(f"Наибольшее значение в паре {y}.")


while not (a := input(f"Введите 1 число: ")).isdecimal() \
        or not (b := input(f"Введите 2 число: ")).isdecimal():
    print("Вы ввели не число.")

else:
    a = int(a)
    b = int(b)
    myf1(a, b)
