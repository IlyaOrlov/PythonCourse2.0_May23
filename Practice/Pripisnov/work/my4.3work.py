n = ''
while (x := input("Введите число: ")).lower() != "stop":
    if not x.isdigit():
        print("Ошибка!Введите число:")
    else:
        n += x
else:
    print(f"Число равно: {n}")
