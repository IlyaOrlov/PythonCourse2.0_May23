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
m = maxmin(a, b)
print(f"Наибольшее число {m}")


def minmax(a, b):
    if a > b:
        print(f"Большее из введённых чисел a = {a}")
    else:
        print(f"Большее из введённых чисел b = {b}")

minmax(1, 500)

