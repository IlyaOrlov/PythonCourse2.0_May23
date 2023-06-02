while (i := input("Введите число: ")).lower() != "stop":
    if i.isdigit():
        print(f" Число: {i}")
    else:
        print("Ошибка! Введите только число ")

print("До встречи")
