x = input("Введите пятизначное число: ")
if x.isnumeric() and len(x)==5:
    for i in range(len(x)):
        print(f"{i + 1} цифра равна {x[i]}")