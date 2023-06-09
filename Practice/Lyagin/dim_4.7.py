def out_decor(fun):
    def decor(*args, **kwargs):
        print("===========")
        rez = fun(*args, **kwargs)
        print("===========")
        return rez
    return decor


@out_decor
def maxmin(a, b):
    if a > b:
        print(f"Большее из введённых чисел a = {a}")
        s = a
    else:
        print(f"Большее из введённых чисел b = {b}")
        s = b
    return s


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
maxmin(a, b)
