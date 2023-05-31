a = input("Введите пятизначное число: ")
while a != len(a) != 5 or not a.isdigit():
    if len(a) != 5 or not a.isdigit():
        print("Число не пятизначное или это не число.")

    a = input("Введите пятизначное число: ")

else:
    print(f"Число: {a}")
    for i, j in enumerate(a):
        print(f"{i+1} цифра ровна {j}")
