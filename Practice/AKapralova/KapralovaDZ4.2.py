while len((a := input("Введите пятизначное число: "))) != 5 or not a.isdigit():
    if len(a) != 5 or not a.isdigit():
        print("Число не пятизначное или это не число.")


else:
    print(f"Число: {a}")
    for i, j in enumerate(a, 1):
        print(f"{i} цифра ровна {j}")
