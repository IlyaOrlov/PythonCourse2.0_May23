x = input("Введите пятизначное число: ")
if x.isnumeric() and len(x) == 5:
    for i, n in enumerate(x, 1):
        print(f"{i} цифра равна {n}")